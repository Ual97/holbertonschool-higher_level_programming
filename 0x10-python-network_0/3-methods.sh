#!/bin/bash
#bash script that displays all methods supported by server
curl -siX "OPTIONS" "$1" | grep 'Allow:' | cut -f2- -d ' '
