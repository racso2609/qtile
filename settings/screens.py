from libqtile import bar, qtile, widget
from libqtile.config import Screen

from settings.constants import screen_affinity
from settings.keys import MENU
from settings.theme import get_color
from settings.utils import battery_icon, eww_open

font = "Caskaydia Cove Nerd Font"


def power():
    eww_open("power_overlay")
    eww_open("power_menu")


def search():
    qtile.cmd_spawn(MENU)


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=5),
                widget.TextBox(
                    fmt="  ",
                    font=font,
                    fontsize=20,
                    foreground=get_color("foreground"),
                    mouse_callbacks={"Button1": power},
                ),
                widget.Spacer(length=5),
                widget.CurrentLayoutIcon(
                    foreground=get_color("foreground"), fmt="{}", font=font, scale=0.5
                ),
                widget.GroupBox(
                    visible_groups=screen_affinity[0],
                    fontsize=24,
                    borderwidth=3,
                    highlight_method="line",
                    # color when have things inside but not active
                    active=get_color("Gray"),
                    # color when view is active
                    block_highlight_text_color=get_color("Magenta"),
                    # color when view doesn't have anything
                    inactive=get_color("DarkGray"),
                    # background active views
                    ## monitor
                    this_current_screen_border=get_color("Magenta"),
                    this_screen_border=get_color("Magenta"),
                    ## laptop
                    other_current_screen_border=get_color("Yellow"),
                    other_screen_border=get_color("Yellow"),
                    ## color with notifications
                    # urgent
                    urgent_border=get_color("DarkMagenta"),
                    rounded=True,
                    disable_drag=True,
                ),
                widget.Spacer(
                    length=8,
                    background=get_color("DarkGray"),
                ),
                widget.TextBox(
                    font=font,
                    fmt="  ",
                    margin=3,
                    background=get_color("DarkGray"),
                    foreground=get_color("Magenta"),
                    mouse_callbacks={"Button1": search},
                    fontsize=12,
                ),
                widget.Spacer(
                    length=8,
                    background=get_color("DarkGray"),
                ),
                widget.WindowName(
                    background=get_color("DarkGray"),
                    format="{name}",
                    fmt=" {}",
                    font=font,
                    foreground=get_color("foreground"),
                    empty_group_string="Desktop",
                    fontsize=13,
                ),
                widget.Spacer(
                    length=6,
                    background="#282738",
                ),
                widget.Systray(background="#282738", fontsize=2, padding=6),
                widget.Spacer(
                    length=6,
                    background="#282738",
                ),
                widget.Spacer(
                    length=6,
                    background=get_color("DarkGreen"),
                ),
                widget.Net(
                    format=" {up}   {down} ",
                    background=get_color("DarkGreen"),
                    foreground=get_color("Gray"),
                    font=font,
                    prefix="k",
                    scroll_fixed_width=True,
                ),
                widget.Spacer(
                    length=6,
                    background=get_color("DarkGreen"),
                ),
                #
                # Battery
                widget.GenPollText(
                    fmt="{}",
                    font=font,
                    foreground=get_color("Magenta"),
                    func=battery_icon,
                    fontsize=13,
                    update_interval=10,
                ),
                widget.Spacer(length=-5),
                widget.Battery(
                    font=font,
                    foreground=get_color("Magenta"),
                    format="{percent:2.0%}",
                    fontsize=13,
                ),
                widget.Spacer(
                    length=10,
                ),
                # memory
                widget.Memory(
                    format="\uf0c7{MemUsed: .0f}{mm}",
                    font=font,
                    fontsize=13,
                    padding=10,
                    background=get_color("DarkGray"),
                ),
                # Volume
                widget.Spacer(
                    length=10,
                    background=get_color("DarkMagenta"),
                ),
                widget.Volume(
                    font=font,
                    background=get_color("DarkMagenta"),
                    foreground=get_color("DarkYellow"),
                    fontsize=13,
                    emoji=True,
                    margin=2,
                ),
                widget.Volume(
                    margin=3,
                    font=font,
                    background=get_color("DarkMagenta"),
                    foreground=get_color("DarkYellow"),
                    fontsize=13,
                ),
                widget.Spacer(
                    length=10,
                    background=get_color("DarkMagenta"),
                ),
                # Clock
                widget.TextBox(
                    fmt="  ",
                    background=get_color("Green"),
                    margin_y=6,
                    margin_x=5,
                    fontsize=20,
                ),
                widget.Spacer(
                    length=-5,
                ),
                widget.Clock(
                    background=get_color("Green"),
                    format="%I:%M %p",
                    font=font,
                    fontsize=13,
                ),
                widget.Spacer(
                    length=10,
                    background=get_color("Green"),
                ),
            ],
            30,
            background=get_color("background"),
            border_width=[0, 0, 0, 0],
            margin=[15, 60, 6, 60],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=24,
                    borderwidth=3,
                    highlight_method="line",
                    # color when have things inside but not active
                    active=get_color("Gray"),
                    # color when view is active
                    block_highlight_text_color=get_color("Magenta"),
                    # color when view doesn't have anything
                    inactive=get_color("DarkGray"),
                    # background active views
                    # monitor
                    this_current_screen_border=get_color("Magenta"),
                    this_screen_border=get_color("Magenta"),
                    # laptop
                    other_current_screen_border=get_color("Yellow"),
                    other_screen_border=get_color("Yellow"),
                    # color with notifications
                    # urgent
                    urgent_border=get_color("DarkMagenta"),
                    rounded=True,
                    disable_drag=True,
                    visible_groups=screen_affinity[1],
                ),
                widget.Spacer(length=5),
                widget.WindowName(
                    background=get_color("DarkGray"),
                    format="{name}",
                    fmt=" {}",
                    font=font,
                    foreground=get_color("foreground"),
                    empty_group_string="Desktop",
                    fontsize=13,
                ),
            ],
            30,
            background=get_color("background"),
            border_width=[0, 0, 0, 0],
            # margin=[15, 60, 6, 60],
        ),
    ),
]
