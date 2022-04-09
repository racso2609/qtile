import os
# import re
import socket
# from typing import List  # noqa: F401
from libqtile import layout, widget

from libqtile.config import Match




def init_layout_theme():
    return {
        "margin": 5,
        "border_width": 2,
        "border_focus": "#5e81ac",
        "border_normal": "#4c566a"
    }


layout_theme = init_layout_theme()

layouts = [
    # layout.MonadTall(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    layout.Columns(margin=8,
                   border_width=2,
                   border_focus="#5e81ac",
                   border_normal="#4c566a"),
    # layout.MonadWide(margin=8, border_width=2, border_focus="#5e81ac", border_normal="#4c566a"),
    # layout.Matrix(**layout_theme),
    # layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]


# COLORS FOR THE BAR
#Theme name : ArcoLinux Zion
def init_colors():
    return [
        ["#4a4a46", "#4a4a46"],  # color 0
        ["#4a4a46", "#4a4a46"],  # color 1
        ["#e3bbf1", "#e3bbf1"],  # color 2
        ["#d33682", "#d33682"],  # color 3
        ["#3384d0", "#3384d0"],  # color 4
        ["#fdf6e3", "#fdf6e3"],  # color 5
        ["#d42121", "#d42121"],  # color 6
        ["#62FF00", "#62FF00"],  # color 7
        ["#9742b5", "#9742b5"],  # color 8
        ["#002b36", "#002b36"]
    ]  # color 9


colors = init_colors()
# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(font="Noto Sans", fontsize=12, padding=2, background=colors[1])


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.GroupBox(font="FontAwesome",
                        fontsize=16,
                        margin_y=-1,
                        margin_x=0,
                        padding_y=6,
                        padding_x=5,
                        borderwidth=0,
                        disable_drag=True,
                        active=colors[9],
                        inactive=colors[5],
                        rounded=False,
                        highlight_method="text",
                        this_current_screen_border=colors[8],
                        foreground=colors[2],
                        background=colors[1]),
        widget.Sep(linewidth=1,
                   padding=10,
                   foreground=colors[2],
                   background=colors[1]),
        widget.CurrentLayout(font="Noto Sans Bold",
                             foreground=colors[5],
                             background=colors[1]),
        widget.Sep(linewidth=1,
                   padding=10,
                   foreground=colors[2],
                   background=colors[1]),
        widget.WindowName(
            font="Noto Sans",
            fontsize=12,
            foreground=colors[5],
            background=colors[1],
        ),
        # widget.Net(
        #          font="Noto Sans",
        #          fontsize=12,
        #          interface="enp0s31f6",
        #          foreground=colors[2],
        #          background=colors[1],
        #          padding = 0,
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.NetGraph(
        #          font="Noto Sans",
        #          fontsize=12,
        #          bandwidth="down",
        #          interface="auto",
        #          fill_color = colors[8],
        #          foreground=colors[2],
        #          background=colors[1],
        #          graph_color = colors[8],
        #          border_color = colors[2],
        #          padding = 0,
        #          border_width = 1,
        #          line_width = 1,
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # # do not activate in Virtualbox - will break qtile
        # widget.ThermalSensor(
        #          foreground = colors[5],
        #          foreground_alert = colors[6],
        #          background = colors[1],
        #          metric = True,
        #          padding = 3,
        #          threshold = 80
        #          ),
        # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
        # widget.Sep(
        # linewidth = 1,
        # padding = 10,
        # foreground = colors[2],
        # background = colors[1]
        # ),
        # arcobattery.BatteryIcon(
        # padding=0,
        # scale=0.7,
        # y_poss=2,
        # theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
        # update_interval = 5,
        # background = colors[1]
        # ),
        # # battery option 2  from Qtile
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        widget.Battery(
            font="Noto Sans",
            update_interval=10,
            fontsize=12,
            foreground=colors[5],
            background=colors[1],
        ),
        # widget.TextBox(
        # font="FontAwesome",
        #          text="  ",
        #          foreground=colors[6],
        #          background=colors[1],
        #          padding = 0,
        #          fontsize=16
        #          ),
        # widget.CPUGraph(
        #          border_color = colors[2],
        #          fill_color = colors[8],
        #          graph_color = colors[8],
        #          background=colors[1],
        #          border_width = 1,
        #          line_width = 1,
        #          core = "all",
        #          type = "box"
        #          ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        # widget.TextBox(
        # font="FontAwesome",
        # text="  ",
        # foreground=colors[4],
        # background=colors[1],
        # padding = 0,
        # fontsize=16
        # ),
        # widget.Memory(
        #          font="Noto Sans",
        #          format = '{MemUsed}M/{MemTotal}M',
        #          update_interval = 1,
        #          fontsize = 12,
        #          foreground = colors[5],
        #          background = colors[1],
        #         ),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        widget.TextBox(font="FontAwesome",
                       text="  ",
                       foreground=colors[3],
                       background=colors[1],
                       padding=0,
                       fontsize=16),
        widget.Clock(foreground=colors[5],
                     background=colors[1],
                     fontsize=12,
                     format="%Y-%m-%d %H:%M"),
        # widget.Sep(
        #          linewidth = 1,
        #          padding = 10,
        #          foreground = colors[2],
        #          background = colors[1]
        #          ),
        widget.Systray(background=colors[1], icon_size=20, padding=4),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2


widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class='Arcolinux-welcome-app.py'),
        Match(wm_class='Arcolinux-tweak-tool.py'),
        Match(wm_class='Arcolinux-calamares-tool.py'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='splash'),
        Match(wm_class='toolbar'),
        Match(wm_class='Arandr'),
        Match(wm_class='feh'),
        Match(wm_class='Galculator'),
        Match(wm_class='arcolinux-logout'),
        Match(wm_class='xfce4-terminal'),
    ],
    fullscreen_border_width=0,
    border_width=0)





