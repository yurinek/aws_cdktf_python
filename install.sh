#!/bin/bash


echo "########## aws cli v2 install"
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install


echo "########## create a named profile (name it CDKFT as shown below)"
aws configure --profile CDKTF


echo "########## install nodejs and npm v16+"
curl -fsSL https://deb.nodesource.com/setup_21.x | sudo -E bash - 
sudo apt-get install -y nodejs


echo "########## install pipenv"
pip3 install pipenv


echo "########## install Terraform CDK"
sudo npm install --global cdktf-cli@latest
