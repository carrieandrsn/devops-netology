#!/bin/bash

ip1=173.194.222.113
ip2=87.250.250.242
ip3=54.241.124.131
alert=false

while ((alert==false))
do
  for ((i=1; i<=3; i++))
  do
    a=ip$i
    curl -m 5 ${!a}:80
    if (($? != 0))
    then
      echo ${!a}: FAILED >> alarm.log
      alert=true
      exit 0
    fi
  done
done