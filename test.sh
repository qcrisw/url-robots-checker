#!/bin/bash

set -e

image_name=qcrisw_url-robots-checker:latest

docker build \
    -f Dockerfile \
    -t $image_name \
    .

if [ ! -d "test-reports" ]; then
    mkdir "test-reports"
fi

docker run \
    --rm \
    -it \
    -v "$PWD"/test-reports:/home/test-reports \
    $image_name \
    /bin/bash -c "python test_runner.py"
