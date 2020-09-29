import boto
from   boto.ec2 import connect_to_region
from   fabric.api import env, run, cd, settings, sudo
from   fabric.api import parallel
import os
import sys

REGION       = os.environ.get("AWS_EC2_REGION")
WEB_ROOT = "/var/www"

# Server user, normally AWS Ubuntu instances have default user "ubuntu"
env.user      = "ubuntu"

# List of AWS private key Files
env.key_filename = ["./flask.pem"]

# Fabric task to restart Apache, runs in parallel
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 restart_apache
# @parallel
# def reload_apache():
# 	sudo('service apache restart')

# Fabric task to start Apache, runs in parallel
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 start_apache
# @parallel
def start_apache():
	with cd("~/Flask_application_with_ec2_instance_docker"):
		sudo('docker-compose up --build -d')

# Fabric task to stop Apache, runs in parallel
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 stop_apache
# @parallel
# def stop_apache():
# 	sudo('sudo docker stop $(sudo docker ps -aq)')

# Fabric task to updates/upgrade OS (Ubuntu), runs in parallel
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 update_os
@parallel
def update_os():
	sudo('apt-get update -y')
	sudo('apt-get upgrade -y')

# Fabric task to reboot OS (Ubuntu), runs in parallel
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 reboot_os
@parallel
def reboot_os():
	sudo('reboot')


# Fabric task for cloning GIT repository in Apache WEB_ROOT
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 update_branch restart_apache
# @parallel
# def clone_branch():
# 	with cd("/var/www"):
# 		run('git pull origin master')

# Fabric task for deploying latest changes using GIT pull
# This assumes that your GIT repository is in Apache WEB_ROOT
# To execute task using fabric run following
# fab set_hosts:phpapp,2X,us-west-1 update_branch restart_apache
# @parallel
def update_branch():
	with cd("~/Flask_application_with_ec2_instance_docker"):
		run('git pull origin master')

# Your custom Fabric task here after and run them using,
# fab set_hosts:phpapp,2X,us-west-1 task1 task2 task3

# Fabric task to set env.hosts based on tag key-value pair
def set_hosts(tag = "Name", value="*", region=REGION):
	key              = "tag:"+tag
	# env.hosts    = _get_public_dns(region, key, value)
	env.hosts = ['ec2-54-170-128-248.eu-west-1.compute.amazonaws.com']

# Private method to get public DNS name for instance with given tag key and value pair
def _get_public_dns(region, key, value ="*"):
	public_dns   = []
	connection   = _create_connection(region)
	# reservations = connection.get_all_instances(filters = {key : value})
	reservations = connection.get_all_instances(
		instance_ids = ['i-062c9d3126aa8e331']
	)
	for reservation in reservations:
		for instance in reservation.instances:
			print("Instance", instance.public_dns_name)
			public_dns.append(str(instance.public_dns_name))
	return public_dns

# Private method for getting AWS connection
def _create_connection(region):
	print("Connecting to ", region)

	conn = connect_to_region(
		region_name = region,
		aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
		aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
	)

	print("Connection with AWS established")
	return conn
