#!/bin/bash

python3 -m venv venv

./venv/bin/pip install wheel
./venv/bin/pip install coverage
./venv/bin/pip install waitress
./venv/bin/pip install pyramid==1.9.4
./venv/bin/pip install repoze.zcml==1.1
./venv/bin/pip install repoze.workflow==1.1
./venv/bin/pip install https://github.com/conestack/cone.app/archive/1.1.zip
./venv/bin/pip install -e .[docs]
