# NoteFormers

Easily Run JupyterLab Notebooks pre-installed with the [Transformers Library](https://huggingface.co/docs/transformers/index) and other popular  NLP frameworks by running a Docker container.

![Alt Text](files/rec.gif)

# Docker Hub
* Docker Hub [hub.docker.com/repository/docker/toluclassics/transformers_notebook](https://hub.docker.com/repository/docker/toluclassics/transformers_notebook)

Docker Pull Command for Docker image with **sagemath Kernel** installed.
```
docker pull toluclassics/transformers_notebook
```

# GitHub
* GitHub [https://github.com/ToluClassics/transformers_notebook](https://https://github.com/ToluClassics/transformers_notebook)

Clone the repository and build the docker image
```
Docker build -t $tag .
```

# Jupyter Docker Stacks - Community Stack version
This project is developed with the helpful guide of [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/). The base container is **jupyter/base-notebook** and this **Community Stack** is setup [via the guide.](https://jupyter-docker-stacks.readthedocs.io/en/latest/contributing/stacks.html)
