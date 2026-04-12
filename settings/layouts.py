from libqtile import layout
from libqtile.config import Match

from settings.theme import get_color


def init_layout_theme():
    return {
        "margin": 5,
        "border_width": 2,
        "border_focus": get_color("Blue"),
        "border_normal": get_color("DarkGray"),
    }


layout_theme = init_layout_theme()

layouts = [
    layout.Columns(
        margin=8,
        border_width=2,
        border_focus=get_color("Blue"),
        border_normal=get_color("DarkGray"),
    ),
    layout.Max(**layout_theme),
]


floating_layout = layout.Floating(
    float_rules=[
        Match(title="flameshot"),
        Match(wm_class="flameshot"),
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Arcolinux-welcome-app.py"),
        Match(wm_class="Arcolinux-tweak-tool.py"),
        Match(wm_class="Arcolinux-calamares-tool.py"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="Arandr"),
        Match(wm_class="feh"),
        Match(wm_class="Galculator"),
        Match(wm_class="arcolinux-logout"),
        Match(wm_class="xfce4-terminal"),
    ],
    fullscreen_border_width=0,
    border_width=0,
)
