FROM ubuntu:20.04
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
LABEL maintainer="kelvinosaigbovo112@gmail.com"

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq --no-install-recommends \
    apt-transport-https \
    apt-utils \
    ca-certificates \
    curl \
    git \
    iputils-ping \
    jq \
    unzip \
    lsb-release \
    software-properties-common \
    libicu66
USER root
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash
VOLUME /myvol1
RUN apt-get install apache2 -y 

EXPOSE 90
COPY file.sh /tmp
WORKDIR /opt
# Can be 'linux-x64', 'linux-arm64', 'linux-arm', 'rhel.6-x64'.
ENV TARGETARCH=linux-x64 
ENV MCPATRAL=Devops
