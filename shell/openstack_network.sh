#!/bin/bash
#创建内外网络 首先需要source keystonec_admin,在openstack环境下执行相应命令
#内网
neutron net-create --router:external=false private2 --provider:network_type vxlan

#neutron subnet-create --name sub_private1 --allocation-pool start=172.151.1.20,end=172.151.1.120 --gateway 172.151.1.1 --dns-nameserver 114.114.114.114 --enable_dhcp=True --ip-version 4 private1 172.151.1.0/24

#neutron net-delete private1

#外网
#neutron net-create --share --router:external=true --provider:network-type flat --provider:physical_network public pub1
