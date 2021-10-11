#!/bin/bash

ip1=192.168.0.1
ip2=173.194.222.113
ip3=87.250.250.242

for ((i=1; i<=3; i++))
do
  a=ip$i  #dynamically set vatiable name
  echo ${!a}: >> host_test1.log
  for ((j=1; j<=5; j++))
  do
    curl ${!a}:80
    if (($? == 0))
    then
      sed -i '$s/$/ OK/' host_test1.log
    else
      sed -i '$s/$/ FAIL/' host_test1.log
    fi
  done
done
