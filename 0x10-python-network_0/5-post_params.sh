#!/bin/bash
#bash script that displays POST request with given parameters
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
