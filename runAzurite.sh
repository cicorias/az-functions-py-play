#!/usr/bin/env bash

# Note replaced by task.json task.

mkdir -p ./.azurite/data

docker run -it --rm -p 10000:10000 -v $(pwd)/.azurite/data:/data \
    mcr.microsoft.com/azure-storage/azurite



 #docker run -it --rm -p 10000:10000 -p 10001:10001 -p 10002:10002 -v $(pwd)/.azurite/data:/opt/azurite/folder cicorias/azureite:2
