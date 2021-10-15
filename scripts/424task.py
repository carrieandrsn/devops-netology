#!/usr/bin/env python3

import socket
import time

service_list = ['drive.google.com', 'mail.google.com', 'google.com']
last_check_result = {}
first_start = True


def get_ip(service):
    current_ip = socket.gethostbyname(service)
    print(service, '-', current_ip)
    if not first_start:
        check_ip(service, current_ip)
    last_check_result[service] = current_ip


def check_ip(service, ip):
    old_ip = last_check_result[service]
    if ip != old_ip:
        print('[ERROR] ' + service + ' IP mismatch: ' + old_ip + ' ' + ip)


while 1 == 1:
    for i in service_list:
        get_ip(i)
    first_start = False
    print()
    time.sleep(10)
