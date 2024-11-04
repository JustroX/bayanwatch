FROM mcr.microsoft.com/vscode/devcontainers/python
RUN apt update && apt upgrade -y && apt install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
apt-get install -y nodejs
CMD sleep infinity
