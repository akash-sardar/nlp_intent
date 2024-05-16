# NLP_INTENT
# End to End implementation of a INTENT classification

## Workflows for all stages - Data Ingestion, Data Validation, Data Transformation
1. Update the ./config/config.yaml
2. Update the ./params.yaml
3. Update the ./entity/__init__.py
4. Update the configuration manager(./src/project_name/config/configuration.py)
5. Update the components (./src/project_name/components/__init__.py)
6. Update the pipeline (./src/project_name/pipeline/__init__.py)
7. Update the main.py
8. Update the app.py


How to run?
STEPS:
Clone the repository

https://github.com/akash-sardar/nlp_intent
STEP 01- Create a conda environment after opening the repository
conda create -n nlp_intent_venv python=3.11 -y
conda activate nlp_intent_venv
STEP 02- install the requirements
pip install -r requirements.txt
# Finally run the following command
python app.py
Now,

open up you local host and port

1. Login to AWS console.
2. Create IAM user for deployment
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
3. Create ECR repo to store/save docker image
- Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one
7. Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-2

AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = simple-app

