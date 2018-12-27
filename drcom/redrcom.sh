#!/bin/bash
# Script to restart drcom.py
# Created by Ekira
# 2017/7/20

drpath="/usr/bin/drcom.py"
drstr="drcom.py"
drval=`ps -ef | grep $drstr | grep -v grep`
drlen=`echo ${#drval}`
drpid=`echo $drval | cut -d ' ' -f2`

if [ $drlen -ne 0 ];then
    echo "Drcom PID is $drpid, now kill it."
    kill -9 $drpid
else
    echo "PID: $drstr not found"
fi
echo "Then restart $drpath"

python2.7 $drpath &
exit 0
