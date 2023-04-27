#!/bin/bash
# bash script for posting json data files to a server
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
