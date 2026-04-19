#!/bin/bash

# export XDG_SESSION_TYPE=x11

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

function deleteIfExist {
  if [[ ! -f $1 ]];then
    notify-send $1
    rm -r -f  $1
    notify-send "Folder deleted" $1 
  fi
}

autorandr -c
# change your keyboard if you need it

# Some ways to set your wallpaper besides variety or nitrogen
# start the conky to learn the shortcuts
# (conky -c $HOME/.config/qtile/scripts/system-overview)&

# starting utility applications at boot time
nm-applet&
# // xfce4-clipman&

picom --config $HOME/.config/picom/picom.conf&
# compton  --config $HOME/.config/qtile/scripts/picom.conf &
# picom --config $HOME/.config/qtile/scripts/picom.conf &

# starting user applications at boot time
# think about nitrogen
nitrogen --restore &
# run caffeine -a &
udiskie&
# telegram-desktop&

# USERNAME=`whoami`
notify-send "Welcome $USERNAME"

# set keyboard language
setxkbmap us
numlockx on
flameshot&


TRASH_FOLDER="$HOME/.local/share/Trash"
IBUS_FOLDER="$HOME/.config/ibus"
CACHE_FOLDER="$HOME/.cache"

deleteIfExist $TRASH_FOLDER
deleteIfExist $IBUS_FOLDER
deleteIfExist $CACHE_FOLDER

# Script para bajar Hz cuando estás en batería
xrandr --output edp-1 --mode 1920x1200 --rate 60.00
notify-send "Safe mode" "Hz reduced to 60 to save battery"

# greenclip daemon

