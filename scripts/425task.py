#!/usr/bin/env python3

import os
import sys
import requests

username = 'carriesqrl'
git_key = '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'
repo = 'devops-netology'
message = sys.argv[1]
current_user = os.popen('whoami').read().strip()
current_date = os.popen("date +'%Y-%m-%d'").read().strip()
branch_name = current_user + '-' + current_date
headers = {'Authorization': "Token " + git_key}

os.chdir(os.path.expanduser('~/devops-netology'))

print('Checking user auth.. \n')
login = requests.get('https://api.github.com', auth=(username, git_key))

print('Adding a new branch.. Name: ' + branch_name)

# get a list of heads in repo
sha_get_url = 'https://api.github.com/repos/' + username + '/' + repo + '/git/refs/heads'
ref_list = requests.get(sha_get_url, headers=headers).json()

# get sha of main branch on which we base the newest one
sha = ref_list[-1]['object']['sha']

# prepare data for add request
add_branch_url = 'https://api.github.com/repos/' + username + '/' + repo + '/git/refs'
ref = "refs/heads/" + branch_name
add_branch_body = {"ref": ref, "sha": sha}

# actually add a branch
requests.post(add_branch_url, json=add_branch_body, headers=headers)
