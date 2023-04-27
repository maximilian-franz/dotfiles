from libqtile.config import Group, Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from .constants import FAVORITES, GROUPS, LAUNCHER_CMD, LOCK_CMD, MOD, POWER_MENU_CMD

terminal = guess_terminal()

groups = [Group(g) for g in GROUPS]

keys = [
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "Tab", lazy.layout.next(), desc="Move focus to other window"),
    KeyChord(
        [MOD],
        "m",
        [
            Key([], "h", lazy.layout.shuffle_left(), desc="Move window to left"),
            Key([], "l", lazy.layout.shuffle_right(), desc="Move window to right"),
            Key([], "j", lazy.layout.shuffle_down(), desc="Move window down"),
            Key([], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        ],
        name="Move Window",
    ),
    KeyChord(
        [MOD],
        "g",
        [
            Key([], "h", lazy.layout.grow_left(), desc="Grow window to left"),
            Key([], "l", lazy.layout.grow_right(), desc="Grow window to right"),
            Key([], "j", lazy.layout.grow_down(), desc="Grow window down"),
            Key([], "k", lazy.layout.grow_up(), desc="Grow window up"),
        ],
        name="Grow Window",
    ),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([MOD], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([MOD], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([MOD], "d", lazy.spawn(LAUNCHER_CMD), desc="Spawn an application"),
    Key([MOD, "shift"], "e", lazy.spawn(POWER_MENU_CMD), desc="Open the power menu"),
    Key([MOD, "shift"], "l", lazy.spawn(LOCK_CMD), desc="Lock the screen"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -D pulse sset Master 1%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -D pulse sset Master 1%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse sset Master toggle")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 1%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 1%-")),
    *(Key([MOD], f"F{i}", lazy.spawn(f)) for i, f in enumerate(FAVORITES, start=1)),
    *[
        group_key
        for g in groups
        for group_key in (
            Key(
                [MOD],
                g.name,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            Key(
                [MOD, "shift"],
                g.name,
                lazy.window.togroup(g.name, switch_group=True),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
        )
    ],
]
