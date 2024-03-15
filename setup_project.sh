#!/bib/bash


echo "########## initialize the CDKTF project using Python template"
mkdir cdktf_python
cd cdktf_python
cdktf init --template="python" --local


echo "########## Activate the project's virtual environment (optional but recommended)"
pipenv shell


echo "########## add provider"
cdktf provider add "aws@~>3.0" 


echo "########## list apps"
cdktf list


echo "########## list installed providers"
cdktf provider list