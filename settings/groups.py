from libqtile.config import Group, Key
from libqtile.lazy import lazy

from settings.constants import group_labels, screen_affinity
from settings.keys import MOD, MOD2, keys

groups = []


for i in range(len(screen_affinity)):
    for j in range(len(screen_affinity[i])):
        groups.append(
            Group(
                name=f"{screen_affinity[i][j]}",
                label=group_labels[int(screen_affinity[i][j])],
                screen_affinity=i,
            )
        )
    # groups.append(
    # Group(
    # name=group_names[i],
    # label=group_labels[i],
    # )
    # )


def go_to_group(name: str):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].toscreen()
            return

        for i in range(len(screen_affinity)):
            if name in screen_affinity[i]:
                qtile.focus_screen(i)
                qtile.groups_map[name].toscreen(i)
                return

    return _inner


for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([MOD], i.name, lazy.function(go_to_group(i.name))),
            Key([MOD, MOD2], i.name, lazy.group[i.name].toscreen()),
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
