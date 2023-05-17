# !/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# change your keyboard if you need it

# Some ways to set your wallpaper besides variety or nitrogen
# start the conky to learn the shortcuts
(conky -c $HOME/.config/qtile/scripts/system-overview) &

# starting utility applications at boot time
nm-applet&

compton &
# compton  --config $HOME/.config/qtile/scripts/picom.conf &
# picom --config $HOME/.config/qtile/scripts/picom.conf &

# starting user applications at boot time
# think about nitrogen
# nitrogen --restore &
# run caffeine -a &
udiskie &
telegram-desktop &
insync start &

USERNAME=`whoami`
notify-send "Welcome $USERNAME"

# set keyboard language
setxkbmap us
numlockx on &

autorandr -c

TRASH_FOLDER="$HOME/.local/share/Trash"
if [[ ! -f $TRASH_FOLDER ]];then
  rm $TRASH_FOLDER
  notify-send "Trash folder deleted"
fi
