#!/bin/bash

long_subject=$(git log --pretty=%s $2..$3 | egrep -m 1 '.{30}')
if [ -n "$long_subject" ]; then
    echo "error: commit subject over 30 characters:"
    echo "    $long_subject"
    exit 1
fi