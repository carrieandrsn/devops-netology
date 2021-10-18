#!/usr/bin/env python3

import sys
import re
import json
import yaml

file_name = sys.argv[1]

# this function will check file extensions based on first symbol
# and will change is_json flag from initially assigned values

def check_file_type(file_name, is_json):
    file = open(file_name, "r")
    first_symbol = file.read(1)
    file.close()
    if (is_json and first_symbol != '{'):
        print("File type mismatch. YAML file in .json \n")
        is_json = False
    elif (not is_json and first_symbol == '{'):
        print("File type mismatch. JSON file in .yml/.yaml \n")
        is_json = True
    else:
        print("File type matches contents. \n")


def json_syntax_check(file_name):
    with open(file_name) as file:
        try:
            json.load(file)
        except json.decoder.JSONDecodeError as err:
            print(f"Invalid JSON: {err}")
            exit()
        else:
            print("Valid JSON \n")


def yaml_syntax_check(file_name):
    with open(file_name) as file:
        try:
            yaml.load(file)
        except yaml.YAMLError as err:
            print(f"Invalid YAML: {err}")
            exit()
        else:
            print("Valid YAML \n")


def json2yaml(file_name):
    new_name = file_name.replace(".json",".yml")
    in_file = open(file_name, "r")
    text = in_file.read()
    in_file.close()
    out_file = open(new_name, "w+")
    yaml.dump(text, out_file)
    out_file.close()


def yaml2json():
    print("placeholder")

# check extensions and exit if invalid
if not bool(re.match(r".*\.(json|yml|yaml)$", file_name)):
    print("Invalid file type")
    exit()
elif bool(re.match(r".*\.(json)$", file_name)):
    is_json = True
else:
    is_json = False

#does it look like contents are correct
print("Checking if file type matches contents \n")
check_file_type(file_name, is_json)

# assuming that we resolve the switch versions, time to check syntax
print("Checking syntax \n")
if is_json:
    json_syntax_check(file_name)
else:
    yaml_syntax_check(file_name)

if is_json:
    print("Converting from JSON to YML \n")
    json2yaml(file_name)
else:
    print("Converting from YML to JSON \n")
    yaml2json(file_name)
