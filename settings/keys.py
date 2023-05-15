import os
from libqtile.config import Key
from libqtile.command import lazy

mod1 = "alt"
mod2 = "control"
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


mod = "mod4"
# terminal = guess_terminal()
terminal = "wezterm"
file_explorer = 'thunar'
explorer = 'brave'

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
    Key([mod], "F1", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([mod], "F3", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([mod], "F2", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([mod, "shift"], "F1", lazy.spawn("playerctl previous")),
    Key([mod, "shift"], "F2", lazy.spawn("playerctl play-pause")),
    Key([mod, "shift"], "F3", lazy.spawn("playerctl next")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +15")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 15-")),
    Key(["control"], "F2", lazy.spawn("brightnessctl s +15")),
    Key(["control"], "F1", lazy.spawn("brightnessctl s 15-")),
    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    # SUPER + SHIFT KEYS
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "r", lazy.restart()),
    # QTILE LAYOUT KEYS
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "Tab", lazy.next_layout()),
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    #    Key([mod, "mod1" ], "f", lazy.layout.flip()),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    # Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),desc="Move window down"),
    # Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Menu
    Key([mod], "space", lazy.spawn("rofi -show drun")),
    Key([mod], "n", lazy.spawn(file_explorer), desc="files"),
    Key([mod, "shift"], "b", lazy.spawn("qutebrowser"), desc="browser"),
    Key([mod], "b", lazy.spawn(explorer), desc="firefox"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="firefox"),
    Key([mod], "r", lazy.spawn("rofi-theme-selector"), desc="firefox"),
    Key([mod], "x", lazy.spawn("arcolinux-logout"), desc="firefox"),
    Key([mod], "a", lazy.spawn("dunstctl close"), desc="close last dunst notification"),
    Key(
        [mod, "shift"],
        "a",
        lazy.spawn("dunstctl close-all"),
        desc="close last dunst notification",
    ),
    # Languages
    Key([mod, "shift"], "e", lazy.spawn("setxkbmap es")),
    Key([mod, "shift"], "u", lazy.spawn("setxkbmap us")),
]
