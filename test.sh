#!/bin/bash

set -e

if [ ! -d "test-reports" ]; then
    mkdir "test-reports"
fi

./run-docker.sh \
    /bin/bash -c "python test_runner.py" \
    -v "$PWD"/test-reports:/home/test-reports
