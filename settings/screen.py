from libqtile.config import Screen
from libqtile import bar
from settings.layouts import myWidgets

def init_screens():
    return [Screen(top=bar.Bar(widgets=myWidgets, size=20, opacity=0.8)),
            Screen(top=bar.Bar(widgets=myWidgets, size=20, opacity=0.8))]

screens = init_screens()

