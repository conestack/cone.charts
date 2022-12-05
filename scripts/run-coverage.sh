#!/bin/bash
./venv/bin/coverage run \
    --source=sources/cone.charts/src/cone/charts \
    -m cone.charts.tests.__init__
./venv/bin/coverage report
./venv/bin/coverage html