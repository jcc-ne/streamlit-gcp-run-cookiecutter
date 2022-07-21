#! /bin/sh
#
# depoy_prod.sh
# Copyright (C) 2021 janine <janine@MacBook-Pro.local>
#
# Distributed under terms of the GNU GPLv3 license.
#


DIR=$(dirname $(python -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' $0))
my_cwd=$PWD

if [ ! $DIR = $PWD ]; then
   echo "need to execute the script from $DIR"
   echo "*** moving to working directory *** "
   echo
   cd $DIR
fi

service_yaml="service.dashboard.yaml"

echo "######### quick view: $service_yaml ####################"
head -5 "../$service_yaml"
echo "####################################################"

confirm_deploy_using_service_yaml() {
    read -p "we are deploying using $service_yaml.  To confirm: type '$service_yaml': " input
    if [ $input != $service_yaml ];then
        confirm_deploy_using_service_yaml
    fi
}

confirm_deploy_using_service_yaml

echo "Deploying using: $service_yaml...($(date +%T))"

cd ..
gcloud builds submit --tag gcr.io/{{cookiecutter.gcp_project_id}}/{{cookiecutter.dashboard_name}}
gcloud beta run services replace $service_yaml

echo "Done Deploying using: $service_yaml. ($(date +%T))"

cd $my_cwd
