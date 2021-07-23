#!/bin/zsh

cd $HOME/Desktop/shared
ifconfig | grep 192.168
python -m http.server
