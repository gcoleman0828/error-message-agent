#!/usr/bin/env bash

echo "permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock" | python3 src/error_classifier.py
