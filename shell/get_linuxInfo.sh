#!/bin/bash
#
# SCRIPT: hwmsg.sh
# DATE: 12/21/2010
# REV: 1.0.1
#
# PURPOSE: This script is used to create a text file that is
#          the exact size specified on the command line.
#
# set -n # Uncomment to check syntax without any execution
# set -x # Uncomment to debug this shell script
#
################################################
# Define files and variables here
################################################
systembit=`getconf LONG_BIT` #系统位数(32或64)
meminfo=`dmidecode | grep "^[[:space:]]*Size.*MB$" | uniq -c | sed 's/ \t*Size: /\*/g' | sed 's/^ *//g'` #内存信息
diskinfo=`fdisk -l|grep Disk|awk '{count+=$3}END{print count$4}'|sed 's/,//g'` #已识别磁盘大小
product_name=`dmidecode | grep "Product Name"| head -1 | awk -F : '{print $2}' | sed 's/^ //'` #设备名称
system_name=`cat /etc/issue|head -n +1` #系统版本
board_name=`dmidecode | grep "Product Name" | tail -n +2 | awk -F : '{print $2}' | sed 's/^ //'` #主板信息
cpu_model=`cat /proc/cpuinfo | grep name | cut -d: -f2 | uniq -c |  sed 's/^ *//'` #CPU型号
cpu_core_num=`cat /proc/cpuinfo | grep "cpu cores" | uniq | awk -F ': ' '{print $2}'` #一个物理CPU的核心数
cpu_phy_num=`cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l` #物理CPU个数
cpu_logic_num=`cat /proc/cpuinfo | grep "siblings" | uniq | awk -F ': ' '{print $2}'` #一个物理CPU的逻辑CPU个数
netcardinfo=`lspci | grep -i eth | head -n +1 | awk -F : '{print $3}' | sed 's/^ //'` #网卡信息
################################################
#   BEGINNING of MAIN
################################################
if [ $cpu_core_num -eq $cpu_logic_num ];then
    echo "+--------------------------------------------+"
    echo "| This Machine's Hyper-Threading is Disabled |" ##超线程已禁用或不支持超线程
    echo "+--------------------------------------------+"
else
    echo "+--------------------------------------------------------------+"
    echo "| This Machine's Hyper-Threading is Enabled(recommend disable) |" ##支持超线程并且已打开（推荐关闭）
    echo "+--------------------------------------------------------------+"
fi
echo "Systembit    :    $systembit"
echo "MEM info     :    $meminfo"
echo "Disk_totle   :    $diskinfo"
echo "Product name :    $product_name"
echo "System name  :    $system_name"
echo "Board name   :    $board_name"
echo "CPU model    :    $cpu_model"
echo "CPU_phy_num  :    $cpu_phy_num"
echo "CPU_core_num :    $cpu_core_num"
echo "CPU_logic_num:    $cpu_logic_num"
echo "Netcard info :    $netcardinfo"
