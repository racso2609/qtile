from libqtile.config import Screen
from libqtile import bar
from settings.layouts import widgets_screen1, widgets_screen2


def init_screens():
    return [
        # Screen(top=bar.Bar(widgets=widgets_screen1, size=26, opacity=0.8)),
        # Screen(
        # top=bar.Bar(widgets=widgets_screen2, size=26, opacity=0.8))
    ]


screens = init_screens()
