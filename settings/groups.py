from libqtile.config import Group, Key
from libqtile.lazy import lazy
from settings.keys import keys, MOD

groups = []

# FOR QWERTY KEYBOARDS
group_names = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
]
group_labels = [
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([MOD], i.name, lazy.group[i.name].toscreen()),
            # Key([MOD], "Tab", lazy.screen.next_group()),
            # Key([MOD, "shift" ], "Tab", lazy.screen.prev_group()),
            # Key(["MOD1"], "Tab", lazy.screen.next_group()),
            # Key(["MOD1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            Key([MOD, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            # Key([MOD, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen() ),
        ]
    )
