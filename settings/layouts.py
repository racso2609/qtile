from libqtile import layout, widget
from libqtile.config import Match

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

