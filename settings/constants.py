MOD = "mod4"
MOD1 = "alt"
MOD2 = "control"

TERMINAL = "wezterm"
FILE_EXPLORER = "nautilus"
EXPLORER = "env -u WAYLAND_DISPLAY XDG_SESSION_TYPE=x11 brave --ozone-platform-hint=x11"
DEV_EXPLORER = "qutebrowser"

SS_TOOL = (
    "env -u WAYLAND_DISPLAY XDG_SESSION_TYPE=x11 QT_QPA_PLATFORM=xcb flameshot gui"
)
MENU = "ulauncher"
MENU_THEME = "rofi-theme-selector"
AUTO_START_SCRIPT_PATH = "~/.config/qtile/scripts/autostart.sh"


floating_types = ["notification", "toolbar", "splash", "dialog", "pop-up"]


# FOR QWERTY KEYBOARDS

group_labels = [
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
    "   ",
]

screen_affinity = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9", "0"],
]
