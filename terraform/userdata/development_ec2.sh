#! /bin/bash

#updating ubuntu instance
sudo apt-get update && sudo apt-get upgrade -y

# installing java
sudo apt install openjdk-11-jre-headless -y

# downloading dependencies for docker
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y

# adding gpg keys
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# installing the docker repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu  $(lsb_release -cs)  stable"

# upgrading the repository
sudo apt-get update && sudo apt-get upgrade -y

# installing latest version of docker
sudo apt-get install docker-ce -y

# changing permissions for the docker socket
sudo chmod 666 /var/run/docker.sock

# starting docker
sudo systemctl start docker

# configure docker to start on boot
sudo systemctl enable docker