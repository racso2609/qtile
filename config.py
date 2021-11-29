from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'),'.config','qtile', 'autostart.sh')])

    
mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

# Volume
   Key ([], "XF86AudioLowerVolume", lazy.spawn(
     "pactl set-sink-volume @DEFAULT_SINK@ -5%"
)),
   Key ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
   Key ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
   Key ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
   Key ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Menu
   Key ([mod], "space", lazy.spawn("rofi -show drun")),

    # Window Nav
   Key ([mod, "shift"], "space", lazy.spawn("rofi -show")),

   Key ([mod], "b", lazy.spawn("qutebrowser"),desc="browser"),
   Key ([mod], "n", lazy.spawn("nautilus"),desc="files"),
   Key ([mod], "f", lazy.spawn("firefox"),desc="firefox"),
   Key ([mod], "s", lazy.spawn("flameshot gui"),desc="firefox"),

]


groups = [Group(i) for i in ["","","歷","ﰪ","",".|."]]

for i, group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], actual_key, lazy.group[group.name].toscreen(),desc="Switch to group"),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name),

            desc="Switch to & move focused window to group "),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(border_focus=['#7745b5', '#7745b5'], border_width=2,fair=True, insert_position=1,margin=4),

    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Caskaydia Cove Nerd Font',
    fontsize=12,
    padding=10,
)
extension_defaults = widget_defaults.copy()
myWidgets =             [
                widget.CurrentLayoutIcon(scale=0.5,background="#7745b5",margin_x=0),
                widget.GroupBox(
                   active=["#ffffff"],
                   inactive = ["#333333"],
                   rounded=False,
                   highlight_method="block",
                   urgent_alert_method="block",
                   urgent_border_color=["#d44866"],
                   this_current_screen_border=["#7745b5"],
                   this_screen_border="#9e999a",
                   disable_drag=False,
                    fontsize=14,
                    margin_x=0,
                    padding_x=14
                ),
                widget.Prompt(),
                widget.WindowName(
                    max_chars=30,
                    format='puto {name}'
                ),

                widget.PulseVolume(),
                widget.Systray(),
                widget.TextBox("default config", name="default"),
                widget.Pomodoro(color_active="#7745b5",color_inactive="#7745b5"),
                widget.Clock(format='  %d/%m/%Y - %H:%M '),
            ]
screens = [
    Screen(
        top=bar.Bar(
myWidgets,
            27,
            opacity = 0.60,
            margin = 0
        ),
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
],border_focus=['#7745b5', '#7745b5'], border_width=3)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True




# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
