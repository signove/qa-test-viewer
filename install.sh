#!/bin/bash

python3 -m pip install --upgrade --user pip setuptools virtualenv

python3 -m virtualenv ./venv
source ./venv/bin/activate

pip3 install -r requirements.txt


