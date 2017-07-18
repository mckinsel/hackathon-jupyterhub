"""Originally from
https://github.com/minrk/jupyterhub-swarm/blob/master/hub-inside/jupyterhub_config.py
"""
import os
from dockerspawner import DockerSpawner

c.JupyterHub.spawner_class = DockerSpawner
# we are passing swarm environment variables in the start command
c.DockerSpawner.use_docker_client_env = True

# The Hub has the hostname 'jupyterhub' on the docker network.
# It will be listening on all ips for internal connections
c.JupyterHub.hub_ip = '0.0.0.0'
c.DockerSpawner.hub_ip_connect = 'jupyterhub'

# these three lines tell the single-user containers
# to join the 'jupyterhub' overlay network,
# and use the container's ip on that network
# when telling the Hub where to find it.
c.DockerSpawner.network_name = 'jupyterhub'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.extra_host_config = {
    'network_mode': 'jupyterhub',
}
c.JupyterHub.db_url = os.path.join("/user_db", "jupyterhub.sqlite")
c.JupyterHub.cookie_secret_file = os.path.join("/user_db", "cookie_secret_file")


from tornado import gen
from jupyterhub.auth import Authenticator

# dummy authenticator for testing. Use a real one (ideally OAuth, etc.)
the_password = 'top secret'
class DummyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
        if data['password'] == the_password:
            return data['username']

c.JupyterHub.authenticator_class = DummyAuthenticator
