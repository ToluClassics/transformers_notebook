ARG TRANSFORMERS_CACHE=/tmp/.cache

FROM cschranz/gpu-jupyter:v1.4_cuda-11.2_ubuntu-20.04_python-only

# Add RUN statements to install packages as the $NB_USER defined in the base images.

# Add a "USER root" statement followed by RUN statements to install system packages using apt-get,
# change file permissions, etc.

# If you do switch to root, always be sure to add a "USER $NB_USER" command at the end of the
# file to ensure the image runs as a unprivileged user by default.

USER root

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir \
    jupyter 

RUN python3 -m pip install transformers datasets tokenizers

USER ${NB_UID}

WORKDIR "${HOME}"