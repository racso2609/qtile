import os
import subprocess
from libqtile import hook

from settings.keys import *
from settings.groups import *
from settings.layouts import *
from settings.mouse import *
from settings.screens import *

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN


#########################################################
################ assign apps to groups ##################
#########################################################
@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    #####################################################################################
    ### Use xprop for find  the value of WM_CLASS(STRING) -> First field is sufficient ###
    #####################################################################################
    d[group_names[0]] = [
        "Navigator",
        "Firefox",
        "Vivaldi-stable",
        "Vivaldi-snapshot",
        "Chromium",
        "Google-chrome",
        "Brave",
        "Brave-browser",
        "navigator",
        "firefox",
        "vivaldi-stable",
        "vivaldi-snapshot",
        "chromium",
        "google-chrome",
        "brave",
        "brave-browser",
    ]
    d[group_names[1]] = [
        "Atom",
        "Subl",
        "Geany",
        "Brackets",
        "Code-oss",
        "Code",
        "TelegramDesktop",
        "Discord",
        "atom",
        "subl",
        "geany",
        "brackets",
        "code-oss",
        "code",
        "telegramDesktop",
        "discord",
    ]
    d[group_names[2]] = ["telegram-desktop", "slack", "Slack"]
    d[group_names[3]] = [
        "Vlc",
        "vlc",
        "Mpv",
        "mpv",
        "Thunar",
        "Nemo",
        "Caja",
        "Nautilus",
        "org.gnome.Nautilus",
        "Pcmanfm",
        "Pcmanfm-qt",
        "thunar",
        "nemo",
        "caja",
        "nautilus",
        "org.gnome.nautilus",
        "pcmanfm",
        "pcmanfm-qt",
    ]
    d[group_names[4]] = [
        "Spotify",
        "Pragha",
        "Clementine",
        "Deadbeef",
        "Audacious",
        "spotify",
        "pragha",
        "clementine",
        "deadbeef",
        "audacious",
    ]
    ######################################################################################

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME

main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.call([home])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
