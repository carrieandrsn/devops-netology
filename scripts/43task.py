#!/usr/bin/env python3

import socket
import time
import json
import yaml

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


def json_yaml_file():
    out_file = open("services.json", "w")
    json.dump(last_check_result, out_file)
    out_file.close()
    out_file = open("services.yaml", "w")
    yaml.dump(last_check_result, out_file)
    out_file.close()


while 1 == 1:
    for i in service_list:
        get_ip(i)
    json_yaml_file()
    first_start = False
    print()
    time.sleep(10)
