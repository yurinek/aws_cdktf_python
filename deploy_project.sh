#!/bin/bash

# To Launch Python virtual environment run this script like this:
# pipenv run ./deploy_project.sh myapp

# to run single commands of this script, execute before:
# pipenv shell
# export PROJECT="myapp"

export PROJECT="$1"

echo "########## Generate CDK Constructs for Terraform providers and modules to the output directory imports"
cdktf get

echo "########## Synthesize Terraform code for the given app into directory cdktf.out"
cdktf synth

echo "########## Perform Terraform Plan"
cdktf diff

echo "########## Perform Terraform Apply"
cdktf deploy --auto-approve

cdktf output

echo "########## To destroy the app resources run the command: cdktf destroy"