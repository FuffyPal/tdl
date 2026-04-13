FROM mcr.microsoft.com/devcontainers/base:trixie

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    golang \
    git \
    git-lfs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git lfs install