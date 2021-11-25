#!/bin/bash

set -e

image_name="saqr_url-robots-checker:latest"
docker build -f Dockerfile -t $image_name .
docker run -it --rm $image_name "$@"
