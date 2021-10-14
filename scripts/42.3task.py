#!/usr/bin/env python3

import os
local = True
repo_path = os.path.expanduser('~/netology/sysadm-homeworks')

query = input('Do you wish to check local repo? y/n \n')
if query == 'n' or query == 'no':
    local = False
    repo_path = input('Please provide path to repo you want to check\n')
elif query != 'y' and query != 'yes':
    print('Not a valid input')
    exit()

if not os.access(repo_path, os.F_OK):
    print("Directory is restricted or doesn't exist")
    exit()

bash_command = ['cd ' + repo_path, 'git status']
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        if local:
            print(os.path.abspath(os.path.expandvars(prepare_result)))
        else:
            print(repo_path + '/' + prepare_result)