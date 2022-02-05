from typing import List  # noqa: F401

from os import path
from libqtile import hook
import subprocess

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
from settings.screen import screens

# from libqtile.log_utils import logger

# @hook.subscribe.startup_once
# def autostart():
    # subprocess.call([path.join(path.expanduser('~'),'.config','qtile', 'autostart.sh')])



# subprocess.call(['~/.config/qtile/scripts/autostart.sh'])

main = None
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')                            
    subprocess.call([home])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
