#!/usr/bin/env bash

# set the wallpaper
nitrogen --restore &
#feh --bg-fill --randomize /path/to/walls

# enable picom
picom --config /home/xtc/.config/qtile/picom.conf

# set correct keymap for me
setxkbmap -layout gb

# enable numlock
numlockx on

