# aws_cdktf_python

This project deploys AWS infrastructure resources using Terraform CDK ( cdktf ) + Python


## Prerequisits

- Linux OS
- Terraform 
- Python 3.7+
- pip3
- AWS account
- access key for AWS user


## Install tools

```
./install.sh
```


## Setup project

```
./setup_project.sh
```


## Deploy project

```
# s3 buckets, ec2 vms, ecs container services are deployed to 3 stages (test, dev, prod)  
./deploy_project.sh
```


## Comparison to plain Terraform

### cdktf advantages

-   the power and flexibility of additional logic of Python can be integrated into infrastructure deployment
-   its possible to add variables into resource names (not possible in Terraform)

### cdktf disadvantages

-   each version of cdktf needs a certain version of nodejs to work properly
-   as of year 2024 still in beta version 0.20.3 with a lot of bugs
-   documentation doesnt keep up with the pace of development of the project. Resulting in outdated documentation.
-   difficult to maintain, to observe internal processes because of the higher abstraction layer (Terraform code is generated from Python code on the fly)
-   employees need to understand Python code
-   variables needs to be defined in Python, which is more complex than Terraform variables
-   no documentation on the names of classes and their attributes
-   no declarative code
-   poor performance: e.g. for "cdktf output" the Terraform code first needs to be synthesized (generated)


## Tested with

Python 3.8.10
cdktf 0.20.3

