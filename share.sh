#!/bin/zsh

cd $HOME/Desktop/shared
IP_ADDR=$(ifconfig | grep 192 | cut -d" " -f 2)
echo "IP Address: $IP_ADDR"
python -m http.server 1337