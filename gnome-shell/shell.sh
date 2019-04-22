#!/bin/bash

./shell-theme.py
glib-compile-resources gnome-shell-theme.gresource.xml
cp gnome-shell-theme.gresource /usr/share/gnome-shell -rf
