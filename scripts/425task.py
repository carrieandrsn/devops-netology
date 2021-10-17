#!/usr/bin/env python3

import os
import sys
import requests

username = 'carriesqrl'
git_key = ''
repo = 'devops-netology'
message = sys.argv[1]
current_user = os.popen('whoami').read().strip()
current_date = os.popen("date +'%Y-%m-%d'").read().strip()
branch_name = current_user + '-' + current_date
headers = {'Authorization': "Token " + git_key}

command = '~/' + repo
os.chdir(os.path.expanduser(command))

print('Checking user auth.. \n')
status = requests.get('https://api.github.com', auth=(username, git_key))
if status.status_code == 200:
    print('Auth successful.. \n')
else:
    print('Auth failed. Please check credentials.')
    exit()

print('Adding a new branch.. Name: ' + branch_name + '\n')

# get a list of heads in repo
url = 'https://api.github.com/repos/' + username + '/' + repo + '/git/refs/heads'
ref_list = requests.get(url, headers=headers).json()

# get sha of main branch on which we base the newest one
sha = ref_list[-1]['object']['sha']

# prepare data for add request
url = 'https://api.github.com/repos/' + username + '/' + repo + '/git/refs'
ref = "refs/heads/" + branch_name
body = {"ref": ref, "sha": sha}

# actually add a branch
status = requests.post(url, json=body, headers=headers)
if status.status_code == 201:
    print('Branch has been added \n')
else:
    print('Branch creation failed')
    exit()

command = 'git pull ' + branch_name
result = os.popen(command).read()

# select newly created branch
command = 'git checkout ' + branch_name
result = os.popen(command).read()

# adding file to commit. Couldn't find how else to mute the output
result = os.popen('git add *').read()

# committing to newly added branch
command = 'git commit -m ' + "'" + message + "'"
result = os.popen(command).read()

command = 'git push origin' + branch_name
result = os.popen(command).read()

# creating pull request
url = 'https://api.github.com/repos/carrieandrsn/' + repo + '/pulls'
pr_branch = username + ':' + branch_name
body = {"head": pr_branch, "base": "main", "title": message}
status = requests.post(url, json=body, headers=headers)
if status.status_code == 201:
    print('Pull request created \n')
else:
    print('Pull request failed')
    exit()
