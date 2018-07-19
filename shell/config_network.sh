#!/bin/bash

#配置文件的修改
f1="/etc/neutron/plugins/ml2/ml2_conf.ini"
f2="/etc/neutron/plugins/ml2/openvswitch_agent.ini"
f3="/etc/neutron/dhcp_agent.ini"
f4="/etc/resolv.conf"

sed -i 's/tenant_network_types.*/tenant_network_types=vlan/g' $f1
sed -i 's/extension_drivers.*/extension_drivers=port_security' $f1
sed -i 's/flat_networks.*/flat_networks=public' $f1
sed -i 's/network_vlan_ranges.*/network_vlan_ranges=public' $f1

sed -i 's/bridge_mappings.*/bridge_mappings=public:br-ex' $f2

sed -i 's/#dhcp_driver.*/dhcp_driver=neutron.agent.linux.dhcp.Dnsmasq' $f3

#重启相关服务
service neutron-dhcp-agent restart
service neutron-openvswitch-agent restart
service neutron-l3-agent restart

#获取ip地址
ip=`ifconfig ens33 | sed -n '/inet /p' | awk '{print $2}'`
gateway=$(cat $f4 | sed -n '/nameserver /p' | awk '{print $2}')

#处理ifcfg文件
cd /etc/sysconfig/network-script/
mv ifcfg-ens33 ifcfg-ens33.bak
touch ifcfg-ens33
touch ifcfg-br-ex

cat > ifcfg-ens33 << END_TEXT
DEVICE=ens33
TYPE=OVSPort
DEVICETYPE=ovs
OVS_BRIDGE=br-ex
ONBOOT=yes

END_TEXT

cat > ifcfg-ens33 << END_TEXT
DEVICE=br-ex
DEVICETYPE=ovs
TYPE=OVSBridge
BOOTPROTO=none
IPADDR=$ip
NETMASK=255.255.255.0
GATEWAY=$gateway
ONBOOT=yes

END_TEXT

echo ">>>>>succeed to change the file"

ovs-vsctl add-br br-ex
ovs-vsctl add-port br-ex ens33

service network restart

echo "network config completed"
