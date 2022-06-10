# reference: https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile
# Dockerfile: https://github.com/jupyter/docker-stacks/blob/master/datascience-notebook/Dockerfile
FROM jupyter/datascience-notebook:2022-06-06

# need to specify root as in the minimal-notebook image the final
# USER command is non-root
USER root

LABEL maintainer="jackhjfission <jackhjfission@gmail.com>"

# set the environment variable
# set the image SSH_AUTH_SOCK to a specific file
ENV SSH_AUTH_SOCK=/ssh-agent/ssh

#Setup File System
ENV HOME="/home/${NB_USER}"
ENV SHELL=/bin/bash

# Install plotly for interactive graphing
RUN arch=$(uname -m) && \
    if [ "${arch}" == "aarch64" ]; then \
        # Prevent libmamba from sporadically hanging on arm64 under QEMU
        # <https://github.com/mamba-org/mamba/issues/1611>
        export G_SLICE=always-malloc; \
    fi && \
    mamba install --quiet --yes \
    'plotly' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# switch back to the jovyan user
USER ${NB_UID}