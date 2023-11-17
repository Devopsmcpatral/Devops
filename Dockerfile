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
ARG Azcopy_version=v10
RUN mkdir -p /opt/hostedtoocache/azcopy/v10 \
    && cd /opt/hostedtoocache/azcopy/v10 \
    && curl -L https://aka.ms/downloadazcopy-${Azcopy_version}-linux | tar --strip-components=1 --exclude=*.txt -xzvf - \
    && rm -rf azcopy_v10.tar.gz \
    && chmod +x azcopy
VOLUME /class/version/azcopy
RUN apt-get install apache2 -y 
RUN mkdir /mcpatral
EXPOSE 90
COPY class1 /mcpatral
WORKDIR /caro
# Can be 'linux-x64', 'linux-arm64', 'linux-arm', 'rhel.6-x64'.
ENV TARGETARCH=linux-x64 
ENV MCPATRAL=Devops
ENV AZCOPY=V10
