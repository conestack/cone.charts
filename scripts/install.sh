#!/bin/bash

if ! which npm &> /dev/null; then
    sudo apt-get install npm
fi

npm --save-dev install \
    qunit \
    karma \
    karma-qunit \
    karma-coverage \
    karma-chrome-launcher \
    karma-module-resolver-preprocessor \
    rollup \
    rollup-plugin-cleanup \
    rollup-plugin-terser \
    jsdoc \
    https://github.com/jquery/jquery#main

JSDOC_BIN="/usr/local/bin/jsdoc"

if [ -L $JSDOC_BIN ] && [ ! -e $JSDOC_BIN ]; then
    sudo rm /usr/local/bin/jsdoc
fi

if [ ! -e $JSDOC_BIN ]; then
    sudo ln -s $(pwd)/node_modules/jsdoc/jsdoc.js $JSDOC_BIN
fi

python3 -m venv venv

./venv/bin/pip install wheel
./venv/bin/pip install coverage
./venv/bin/pip install waitress
./venv/bin/pip install pyramid==1.9.4
./venv/bin/pip install repoze.zcml==1.1
./venv/bin/pip install repoze.workflow==1.1
./venv/bin/pip install https://github.com/conestack/cone.app/archive/1.1.zip
./venv/bin/pip install -e .[docs]
