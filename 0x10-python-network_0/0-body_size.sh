#!/bin/bash
#bash script that displays size of body from url request
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d ' '
