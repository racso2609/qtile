import subprocess
import os

# Full path to theme-compositor CLI
THEME_CLI = os.path.expanduser("~/.npm-global/bin/theme-compositor")

# Cache for colors - avoid calling CLI on every widget
_color_cache = {}


def get_color(color):
    """Get color from theme-compositor, with caching for performance."""
    if color in _color_cache:
        return _color_cache[color]

    try:
        result = subprocess.run(
            [THEME_CLI, "--get-theme-color", color],
            capture_output=True,
            text=True,
            timeout=5,
            env={**os.environ, "HOME": os.environ.get("HOME", "/home/racso")},
        )
        hex_color = result.stdout.strip()
        if hex_color.startswith("#"):
            _color_cache[color] = hex_color
            return hex_color
    except Exception:
        pass

    return _get_fallback_color(color)


def _get_fallback_color(color):
    """Fallback colors in case theme-compositor fails."""
    fallbacks = {
        "background": "#282c34",
        "foreground": "#abb2bf",
        "Black": "#282c34",
        "DarkGray": "#3e4451",
        "DarkGreen": "#3e4451",
        "Gray": "#abb2bf",
        "White": "#c8ccd4",
        "Red": "#e06c75",
        "DarkRed": "#d19a66",
        "Yellow": "#e5c07b",
        "Green": "#98c379",
        "Cyan": "#56b6c2",
        "Blue": "#61afef",
        "Magenta": "#c678dd",
        "DarkMagenta": "#be5046",
    }
    return fallbacks.get(color, "#ffffff")


# Preload colors at module load for faster widget initialization
def init_colors():
    """Initialize common colors into cache."""
    colors_to_preload = [
        "background",
        "foreground",
        "Black",
        "DarkGray",
        "DarkGreen",
        "Gray",
        "White",
        "Red",
        "DarkRed",
        "Yellow",
        "Green",
        "Cyan",
        "Blue",
        "Magenta",
        "DarkMagenta",
    ]
    for color in colors_to_preload:
        get_color(color)


# Load colors when module is imported
init_colors()
