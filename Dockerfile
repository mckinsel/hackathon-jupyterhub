FROM jupyterhub/jupyterhub:0.7.2
RUN pip install dockerspawner
ADD jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
