#!/bin/bash
# Script: SystemInfoToJson.sh
# Purpose: Display the TEMP%, CPU%, MEM% and DISK% of a Raspberry Pi
# -------------------------------------------------------
temp=$(cat /sys/class/thermal/thermal_zone0/temp)
cpu=$(top -b -n1 | grep "Cpu(s)" | awk '{print $2 + $4}')
mem=$(free -t | awk 'NR == 2 {printf("%.1f"), $3/$2*100}')
disk=$(df -hl | grep '/dev/root' | awk '{print $5}' | sed 's/%//')
# -------------------------------------------------------
echo "{"
echo "    \"TEMP\": $((temp/1000)),"
echo "    \"CPU\": $cpu,"
echo "    \"MEM\": $mem,"
echo "    \"DISK\": $disk"
echo '}'
