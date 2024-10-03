from libqtile import bar, qtile, widget
from libqtile.config import Screen

from settings.constants import screen_affinity
from settings.keys import MENU
from settings.theme import get_color
from settings.utils import battery_icon, eww_open

font = "Caskaydia Cove Nerd Font"

SM = 8
MD = 12
LG = 16


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
                    fontsize=MD,
                    foreground=get_color("foreground"),
                    mouse_callbacks={"Button1": power},
                ),
                widget.Spacer(length=SM),
                widget.CurrentLayoutIcon(
                    foreground=get_color("Magenta"),
                    fmt="{}",
                    font=font,
                    scale=0.3,
                    fontsize=MD,
                ),
                widget.Spacer(length=LG),
                # widget.Spacer(
                #     length=SM,
                #     background=get_color("Magenta"),
                # ),
                widget.GroupBox(
                    # visible_groups=screen_affinity[0],
                    borderwidth=1,
                    highlight_method="line",
                    # color when have things inside but not active
                    # active=get_color("Gray"),
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
                    margin=0,
                    padding_x=5,
                    # padding=None,
                    # fontsize=LG,
                ),
                # widget.Spacer(
                #     length=SM,
                #     background=get_color("Green"),
                # ),
                # widget.GroupBox(
                #     visible_groups=screen_affinity[1],
                #     borderwidth=0,
                #     highlight_method="line",
                #     # color when have things inside but not active
                #     active=get_color("Gray"),
                #     # color when view is active
                #     block_highlight_text_color=get_color("Magenta"),
                #     # color when view doesn't have anything
                #     inactive=get_color("DarkGray"),
                #     # background active views
                #     ## monitor
                #     this_current_screen_border=get_color("Magenta"),
                #     this_screen_border=get_color("Magenta"),
                #     ## laptop
                #     other_current_screen_border=get_color("Yellow"),
                #     other_screen_border=get_color("Yellow"),
                #     ## color with notifications
                #     # urgent
                #     urgent_border=get_color("DarkMagenta"),
                #     rounded=True,
                #     disable_drag=True,
                #     margin=0,
                # ),
                widget.TextBox(
                    font=font,
                    fmt="  ",
                    margin=3,
                    background=get_color("DarkGray"),
                    foreground=get_color("Magenta"),
                    mouse_callbacks={"Button1": search},
                    fontsize=MD,
                ),
                widget.Spacer(),
                widget.Spacer(
                    length=SM,
                    background="#282738",
                ),
                widget.Systray(background="#282738", fontsize=2, padding=SM),
                widget.Spacer(
                    length=SM,
                    background="#282738",
                ),
                widget.Spacer(
                    length=SM,
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
                    length=SM,
                    background=get_color("DarkGreen"),
                ),
                #
                # Battery
                widget.GenPollText(
                    fmt="{}",
                    font=font,
                    foreground=get_color("Magenta"),
                    func=battery_icon,
                    fontsize=MD,
                    update_interval=10,
                ),
                widget.Spacer(length=-5),
                widget.Battery(
                    font=font,
                    foreground=get_color("Magenta"),
                    format="{percent:2.0%}",
                    fontsize=MD,
                ),
                widget.Spacer(
                    length=10,
                ),
                # memory
                widget.Memory(
                    format="\uf0c7{MemUsed: .0f}{mm}",
                    font=font,
                    fontsize=MD,
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
                    fontsize=MD,
                    emoji=True,
                    margin=2,
                ),
                widget.Volume(
                    margin=3,
                    font=font,
                    background=get_color("DarkMagenta"),
                    foreground=get_color("DarkYellow"),
                    fontsize=MD,
                ),
                widget.Spacer(
                    length=10,
                    background=get_color("DarkMagenta"),
                ),
                # Clock
                widget.TextBox(
                    fmt="  ",
                    background=get_color("Green"),
                    margin_y=SM,
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
                    fontsize=MD,
                ),
                widget.Spacer(
                    length=10,
                    background=get_color("Green"),
                ),
            ],
            25,
            background=get_color("background"),
            border_width=[0, 0, 0, 0],
            margin=[15, 10, 6, 10],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
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
                widget.WindowName(
                    background=get_color("DarkGray"),
                    format="{name}",
                    fmt=" {}",
                    font=font,
                    foreground=get_color("foreground"),
                    empty_group_string="Desktop",
                    fontsize=MD,
                ),
            ],
            30,
            background=get_color("background"),
            border_width=[0, 0, 0, 0],
            # margin=[15, 60, 6, 60],
        ),
    ),
]
