import os

from libqtile.config import Key
from libqtile.lazy import lazy

from settings.constants import (
    DEV_EXPLORER,
    EXPLORER,
    FILE_EXPLORER,
    MENU,
    MENU_THEME,
    MOD,
    MOD2,
    SS_TOOL,
    TERMINAL,
)
from settings.screens import power

home = os.path.expanduser("~")

# TODO: make it more beautifull
keys = [
    Key(
        ["mod1"],
        "Tab",
        lazy.spawn("rofi -show window"),
    ),
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
    # Key([MOD, "shift"], "n", lazy.layout.normalize()),
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
    # TOGGLE FLOATING LAYOUT
    Key([MOD, "shift"], "f", lazy.window.toggle_floating()),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    # Menu
    Key([MOD], "space", lazy.spawn(MENU)),
    Key([MOD], "n", lazy.spawn(FILE_EXPLORER), desc="files"),
    Key(
        [MOD, "shift"],
        "b",
        lazy.spawn(DEV_EXPLORER),
        desc="dev browser normally to test",
    ),
    Key([MOD], "b", lazy.spawn(EXPLORER), desc="firefox"),
    Key([MOD], "s", lazy.spawn(SS_TOOL), desc="screenshot tool"),
    Key([MOD], "r", lazy.spawn(MENU_THEME), desc="mwnu theme selector"),
    Key(
        [MOD],
        "x",
        power,
        desc="logout menu",
    ),
    Key(
        [MOD2],
        "space",
        lazy.spawn("dunstctl close"),
        desc="close last dunst notification",
    ),
    Key(
        [MOD2, "shift"],
        "space",
        lazy.spawn("dunstctl close-all"),
        desc="close last dunst notification",
    ),
    # Languages
    Key([MOD, "shift"], "e", lazy.spawn("setxkbmap es")),
    Key([MOD, "shift"], "u", lazy.spawn("setxkbmap us")),
]
