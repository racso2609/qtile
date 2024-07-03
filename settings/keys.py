import os
from libqtile.config import Key
from libqtile.lazy import lazy

MOD1 = "alt"
MOD2 = "control"
home = os.path.expanduser("~")


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


MOD = "mod4"
# TERMINAL = guess_terminal()
TERMINAL = "wezterm"
# TERMINAL = "alacritty"
FILE_EXPLORER = "nautilus"
# EXPLORER = "firefox"
EXPLORER = "brave"

# TODO: make it more beautifull
keys = [
    # notification control
    Key(
        ["control"],
        "space",
        lazy.spawn("dunstctl close"),
    ),
    Key(
        ["control", "shift"],
        "space",
        lazy.spawn("dunstctl close-all"),
    ),
    # Most of our keybindings are in sxhkd file - except these
    # Volume
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([MOD], "F1", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([MOD], "F3", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([MOD], "F2", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([MOD, "shift"], "F1", lazy.spawn("playerctl previous")),
    Key([MOD, "shift"], "F2", lazy.spawn("playerctl play-pause")),
    Key([MOD, "shift"], "F3", lazy.spawn("playerctl next")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +15")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 15-")),
    Key(["control"], "F2", lazy.spawn("brightnessctl s +15")),
    Key(["control"], "F1", lazy.spawn("brightnessctl s 15-")),
    # SUPER + FUNCTION KEYS
    Key([MOD], "f", lazy.window.toggle_fullscreen()),
    Key([MOD], "q", lazy.window.kill()),
    # SUPER + SHIFT KEYS
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD, "control"], "r", lazy.restart()),
    # QTILE LAYOUT KEYS
    Key([MOD, "shift"], "n", lazy.layout.normalize()),
    Key([MOD], "Tab", lazy.next_layout()),
    # CHANGE FOCUS
    Key([MOD], "Up", lazy.layout.up()),
    Key([MOD], "Down", lazy.layout.down()),
    Key([MOD], "Left", lazy.layout.left()),
    Key([MOD], "Right", lazy.layout.right()),
    Key([MOD], "k", lazy.layout.up()),
    Key([MOD], "j", lazy.layout.down()),
    Key([MOD], "h", lazy.layout.left()),
    Key([MOD], "l", lazy.layout.right()),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key(
        [MOD, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [MOD, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [MOD, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [MOD, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [MOD, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [MOD, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [MOD, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [MOD, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    #    Key([MOD, "mod1" ], "f", lazy.layout.flip()),
    # FLIP LAYOUT FOR BSP
    Key([MOD, "mod1"], "k", lazy.layout.flip_up()),
    Key([MOD, "mod1"], "j", lazy.layout.flip_down()),
    Key([MOD, "mod1"], "l", lazy.layout.flip_right()),
    Key([MOD, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up()),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down()),
    Key([MOD, "shift"], "h", lazy.layout.shuffle_left()),
    Key([MOD, "shift"], "l", lazy.layout.shuffle_right()),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([MOD, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([MOD, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([MOD, "shift"], "Left", lazy.layout.swap_left()),
    Key([MOD, "shift"], "Right", lazy.layout.swap_right()),
    # Moving out of range in Columns layout will create new column.
    Key(
        [MOD, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [MOD, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    # Key([MOD, "shift"], "Down", lazy.layout.shuffle_down(),desc="Move window down"),
    # Key([MOD, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # TOGGLE FLOATING LAYOUT
    Key([MOD, "shift"], "f", lazy.window.toggle_floating()),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    # Menu
    Key([MOD], "space", lazy.spawn("rofi -show drun")),
    Key([MOD], "n", lazy.spawn(FILE_EXPLORER), desc="files"),
    Key([MOD, "shift"], "b", lazy.spawn("qutebrowser"), desc="browser"),
    Key([MOD], "b", lazy.spawn(EXPLORER), desc="firefox"),
    Key([MOD], "s", lazy.spawn("flameshot gui"), desc="firefox"),
    Key([MOD], "r", lazy.spawn("rofi-theme-selector"), desc="firefox"),
    Key([MOD], "x", lazy.spawn("arcolinux-logout"), desc="firefox"),
    Key([MOD], "c", lazy.spawn("dunstctl close"), desc="close last dunst notification"),
    Key(
        [MOD, "shift"],
        "c",
        lazy.spawn("dunstctl close-all"),
        desc="close last dunst notification",
    ),
    # Languages
    Key([MOD, "shift"], "e", lazy.spawn("setxkbmap es")),
    Key([MOD, "shift"], "u", lazy.spawn("setxkbmap us")),
]
