#!/bin/zsh

cd $HOME/Desktop/shared
ifconfig | grep 192 | cut -f 2 -d" "
python -m http.server
