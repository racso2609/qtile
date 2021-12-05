from libqtile.config import Group, Key
from libqtile.lazy import lazy
from settings.keys import keys, mod

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


