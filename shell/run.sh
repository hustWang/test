#!/bin/bash

#读取配置文件的内容
username=$(cat config.ini |grep username | awk -F'= ' '{print $2}' |sed s/[[:space:]]//g)
echo $username
mkdir $username

#创建Vagrantfile文件
cd $username
touch Vagrantfile

cat > Vagrantfile << END_TEXT
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.ssh.username = 'centos'
  config.vm.box = "dummy3"
  config.ssh.private_key_path = "~/.ssh/id_rsa"
  config.vm.provider :openstack do |os|
    os.tenant_name                     =    'default'
    os.openstack_auth_url              =    ENV['OS_AUTH_URL']
#    os.endpoint                        =    ENV['OS_AUTH_URL']/tokens
    os.server_name                     =    '$username'
    os.identity_api_version            =    '3'
    os.project_name                    =    ENV['OS_PROJECT_NAME']
    os.username                        =    ENV['OS_USERNAME']
    os.password                        =    ENV['OS_PASSWORD']
    os.flavor                          =    'm1.d1'
    os.image                           =    'centos7'
#    os.domain_id                       =    'default'
    os.domain_name                     =    'Default'
  os.keypair_name                    =    'default'
   # os.floating_ip                     =    :auto
  #  os.floating_ip_pool                =    'EXTNET'
  end
end
END_TEXT

#openstack 的环境变量
cd ~

source keystonerc_admin

cd $username
vagrant up
