# END-TO-END-ML-PROJECT

Project -
US VISA APPROVAL PREDICTION


# git command
  Before starting git execution, need to set github username and email -

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

1. git add <file_name>
2. git commit -m 'commit msg'
3. git push origin main

# create env

1. conda create -n visa python=<version> -y
# eg conda create -n visa1 python=3.11 -y
2. conda activate visa1condava

# to install requirements
1. pip install -r requirements.txt



install driver
python -m pip install "pymongo[srv]"==3.6

# Env variable
export AWS_ACCESS_KEY_ID = <AWS ACCESS KEY ID>
export AWS_SECRET_ACCESS_KEY = <AWS SECRETE KEY ID>



# workflow
1. constant
2. config_entity
3. artifact_entity
4. components
5. pipeline
6. app.py

# Data validation
1. added schema.yaml

## AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

- Save the URI: 008971679870.dkr.ecr.us-east-1.amazonaws.com/usvisa

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker


## 6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_DEFAULT_REGION
ECR_REPO
