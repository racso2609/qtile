import itertools
import os
import subprocess

from libqtile import hook

from settings.constants import AUTO_START_SCRIPT_PATH, floating_types, screen_affinity

group_names = itertools.chain(*screen_affinity)


@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    ##################################################
    # Use xprop for find  the value of WM_CLASS(STRING)#
    # -> First field is sufficient                     #
    ##################################################
    d[group_names[0]] = [
        # "Navigator",
        # "Firefox",
        # "Vivaldi-stable",
        # "Vivaldi-snapshot",
        # "Chromium",
        # "Google-chrome",
        # "Brave",
        # "Brave-browser",
        # "navigator",
        # "firefox",
        # "vivaldi-stable",
        # "vivaldi-snapshot",
        # "chromium",
        # "google-chrome",
        # "brave",
        # "brave-browser",
    ]
    d[group_names[1]] = [
        "Atom",
        "Subl",
        "Geany",
        "Brackets",
        "Code-oss",
        "Code",
        "atom",
        "subl",
        "geany",
        "brackets",
        "code-oss",
        "code",
    ]
    d[group_names[2]] = []
    d[group_names[3]] = [
        "telegram-desktop",
        "slack",
        "Slack",
    ]
    d[group_names[4]] = [
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
    d[group_names[5]] = [
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
        "youtube",
    ]
    #####################################################################

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            client.group.cmd_toscreen(toggle=False)


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser(AUTO_START_SCRIPT_PATH)
    subprocess.call([home])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
        or window.window.get_wm_window_role() in floating_types
    ):
        window.floating = True
