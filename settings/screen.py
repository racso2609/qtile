from libqtile.config import Screen
from libqtile import bar
from settings.layouts import myWidgets

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
