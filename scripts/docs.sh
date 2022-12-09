#!/bin/bash

export PATH=$PATH:$(pwd)/node_modules/jsdoc
./venv/bin/sphinx-build docs/source docs/html

