from libqtile.config import Drag
from libqtile.lazy import lazy
from settings.keys import mod

# MOUSE CONFIGURATION
mouse = [
    Drag([mod],
         "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]
