from libqtile import bar, qtile, widget
from libqtile.config import Screen

from settings.constants import screen_affinity, TERMINAL
from settings.keys import MENU
from settings.theme import get_color
from settings.utils import battery_icon, eww_open, execute_command
from datetime import datetime

font = "JetBrainsMono Nerd Font"

SM = 6
MD = 12
LG = 14


from libqtile.lazy import lazy


# --- Callbacks ---
def power():
    eww_open("power_overlay")
    eww_open("power_menu")


def chang_clock_format():
    actual_date = datetime.today().strftime("%d-%m-%Y")
    execute_command("notify-send " + str(actual_date))


# --- Transparent Background ---
# Append hex alpha 'CC' (80% opacity) to the theme's background color
# E.g. "#282c34" -> "#282c34CC"
bg_transparent = get_color("background")
if len(bg_transparent) == 7:
    bg_transparent += "CC"

# --- Reusable Widgets ---
clock_widget = [
    widget.Clock(
        format="  %H:%M",
        font=font,
        fontsize=MD,
        foreground=get_color("Magenta"),
        padding=8,
        mouse_callbacks={"Button1": chang_clock_format},
    ),
]


def simple_separator(length=12):
    """Transparent spacer for clean breathing room"""
    return widget.Spacer(
        length=length,
        background=bg_transparent,
    )


# --- Screens ---
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.TextBox(
                    text="⏻",
                    font=font,
                    fontsize=16,
                    foreground=get_color("Red"),
                    mouse_callbacks={"Button1": power},
                    padding=4,
                ),
                simple_separator(15),
                widget.GroupBox(
                    font=font,
                    fontsize=LG,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=4,
                    borderwidth=0,
                    inactive=get_color("DarkGray"),
                    active=get_color("foreground"),
                    rounded=False,
                    highlight_method="text",
                    this_current_screen_border=get_color("Magenta"),
                    this_screen_border=get_color("Magenta"),
                    other_current_screen_border=get_color("Yellow"),
                    other_screen_border=get_color("Yellow"),
                    urgent_border=get_color("Red"),
                ),
                simple_separator(20),
                widget.WindowName(
                    format="{name}",
                    font=font,
                    fontsize=MD,
                    foreground=get_color("Gray"),
                    empty_group_string="",
                    max_chars=60,
                ),
                widget.Spacer(),
                widget.Systray(
                    padding=10,
                    icon_size=20,
                    background=bg_transparent,
                ),
                simple_separator(15),
                widget.Net(
                    interface="all",
                    format="    {down}",
                    font=font,
                    fontsize=MD,
                    foreground=get_color("Cyan"),
                    mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e nmtui-go")},
                ),
                simple_separator(15),
                widget.CPU(
                    format="    {load_percent}%",
                    font=font,
                    fontsize=MD,
                    foreground=get_color("Red"),
                    mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e htop")},
                ),
                simple_separator(15),
                widget.Memory(
                    format="  {MemUsed: .0f}G",
                    font=font,
                    fontsize=MD,
                    foreground=get_color("Yellow"),
                    measure_mem="G",
                    mouse_callbacks={"Button1": lazy.spawn(f"{TERMINAL} -e htop")},
                ),
                simple_separator(15),
                widget.Volume(
                    font=font,
                    fontsize=MD,
                    foreground=get_color("Blue"),
                    emoji=False,
                    volume_app="pulseaudio",
                    volume_down_char="",
                    volume_up_char="",
                    mute_char="",
                    mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
                ),
                simple_separator(15),
                widget.Battery(
                    font=font,
                    fontsize=MD,
                    foreground=get_color("Green"),
                    format="{char}    {percent:2.0%}",
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    full_char="",
                    unknown_char="",
                    show_short_text=False,
                ),
                simple_separator(15),
                *clock_widget,
            ],
            30,
            background=bg_transparent,
            border_width=[0, 0, 0, 0],
            margin=[8, 12, 4, 12],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.GroupBox(
                    font=font,
                    fontsize=LG,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=4,
                    borderwidth=0,
                    inactive=get_color("DarkGray"),
                    active=get_color("foreground"),
                    highlight_method="text",
                    this_current_screen_border=get_color("Magenta"),
                    visible_groups=(
                        screen_affinity[1] if len(screen_affinity) > 1 else []
                    ),
                ),
                widget.Spacer(),
                *clock_widget,
            ],
            30,
            background=bg_transparent,
            border_width=[0, 0, 0, 0],
            margin=[8, 12, 4, 12],
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.GroupBox(
                    font=font,
                    fontsize=LG,
                    margin_y=3,
                    margin_x=0,
                    padding_y=5,
                    padding_x=4,
                    borderwidth=0,
                    inactive=get_color("DarkGray"),
                    active=get_color("foreground"),
                    highlight_method="text",
                    this_current_screen_border=get_color("Magenta"),
                    visible_groups=(
                        screen_affinity[2] if len(screen_affinity) > 2 else []
                    ),
                ),
                widget.Spacer(),
                *clock_widget,
            ],
            30,
            background=bg_transparent,
            border_width=[0, 0, 0, 0],
            margin=[8, 12, 4, 12],
        ),
    ),
]
