# -*- coding: utf-8 -*-

# imports for window manager
import os
import re
import socket
import subprocess
import string
from typing import List # noqa: F401
from libqtile import layout, bar, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, Rule
from libqtile.command import lazy
from libqtile.widget import Spacer
#import xtcbattery

# variables for the window manager 
mod = "mod4"

# application variables
alacritty = "alacritty"
xfce4_terminal = "xfce4-terminal"
firefox = "firefox"
thunar = "thunar"
rofi = "rofi -show drun"
dmenu = "dmenu_run"
telegram_desktop = "telegram-desktop"
idea = "idea"
vscode = "code"

@hook.subscribe.startup_once
def autostart_script():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])

@lazy.function
def move_window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

@lazy.function
def move_window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)

def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)

keys = [

    # Application Keybindings
    Key([mod], "Return", lazy.spawn(alacritty)),
    Key([mod], "p", lazy.spawn(rofi)),
    Key([mod], "w", lazy.spawn(firefox)),
    Key([mod], "Return", lazy.spawn(alacritty)),
    Key(["control", "mod1"], "t", lazy.spawn(xfce4_terminal)),
    Key([mod, "shift"], "p", lazy.spawn(dmenu)),
    Key([mod, "shift"], "Return", lazy.spawn(thunar)),
    Key([mod, "shift"], "t", lazy.spawn(telegram_desktop)),
    Key([mod, "shift"], "i", lazy.spawn(idea)),
    Key([mod, "shift"], "v", lazy.spawn(vscode)),

    # QTile keybindings

    # Kill a focused window
    Key([mod, "shift"], "c", lazy.window.kill()),

    # Move window to next screen
    Key([mod,"shift"], "Right", lazy.function(window_to_next_screen, switch_screen=True)),
    Key([mod,"shift"], "Left", lazy.function(window_to_previous_screen, switch_screen=True)),


]

groups = list(string.digits)