#!/usr/bin/env python

# for CDK
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput

# for terraform provider
from imports.aws.provider import AwsProvider
from imports.aws.instance import Instance

# for terraform module
from imports.aws.s3_bucket import S3Bucket
from imports.aws.ecs_cluster import EcsCluster
from imports.aws.ec2_host import Ec2Host

# additional imports
from randomstr import str_generator
import os
import sys

try:  
   os.environ["PROJECT"]
except KeyError: 
   print ("Please set the environment variable PROJECT")
   sys.exit(1)

project = os.environ["PROJECT"]
print("PROJECT: " + os.environ["PROJECT"])
# store random string, so all the resources for this run have the same random string in their name
str_generated = str_generator()
print("str_generated: " + str_generated)



class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # provider
        AwsProvider(self, 'Aws', region='eu-central-1', profile='CDKTF')

        stages = ["test", "dev", "prod"]
        for stage in stages:
            print("########## Processing infrastructure for the following stage: " + stage + " ...")  

            # s3 bucket
            S3Bucket(self, 's3-{}-{}'.format(project, stage), bucket= project + "-s3-bucket-" + stage + "-" + str_generated)

            # simplest elastic container service required config
            my_ecs_cluster = EcsCluster(self, 'ecs-{}-{}'.format(project, stage),
            name = project + "-ecs-" + stage
            )

            # ec2 virtual machine
            instance = Instance(self, 'ec2-{}-{}'.format(project, stage),
                                ami="ami-042e6fdb154c830c5",
                                instance_type="t2.nano",
                                tags={"Name": project + "-ec2-" + stage},
                                )

            TerraformOutput(self, 'public_ip-{}-{}'.format(project, stage),
                            value=instance.public_ip,
                            )


app = App()
MyStack(app, "cdktf_python")
app.synth()


