from libqtile.config import Group, Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from .settings import Settings
from .utils import change_brightness, change_volume, toggle_mute

terminal = guess_terminal()

groups = [Group(g) for g in Settings.groups]


keys = [
    Key([Settings.mod_key], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([Settings.mod_key], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([Settings.mod_key], "j", lazy.layout.down(), desc="Move focus down"),
    Key([Settings.mod_key], "k", lazy.layout.up(), desc="Move focus up"),
    Key(
        [Settings.mod_key], "Tab", lazy.layout.next(), desc="Move focus to other window"
    ),
    KeyChord(
        [Settings.mod_key],
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
        [Settings.mod_key],
        "g",
        [
            Key([], "h", lazy.layout.grow_left(), desc="Grow window to left"),
            Key([], "l", lazy.layout.grow_right(), desc="Grow window to right"),
            Key([], "j", lazy.layout.grow_down(), desc="Grow window down"),
            Key([], "k", lazy.layout.grow_up(), desc="Grow window up"),
        ],
        name="Grow Window",
    ),
    Key(
        [Settings.mod_key], "n", lazy.layout.normalize(), desc="Reset all window sizes"
    ),
    Key([Settings.mod_key], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([Settings.mod_key], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([Settings.mod_key], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [Settings.mod_key, "control"],
        "r",
        lazy.reload_config(),
        desc="Reload the config",
    ),
    Key([Settings.mod_key, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [Settings.mod_key],
        "d",
        lazy.spawn(Settings.commands.launcher),
        desc="Spawn an application",
    ),
    Key(
        [Settings.mod_key],
        "e",
        lazy.spawn(Settings.commands.power_menu),
        desc="Open the power menu",
    ),
    Key(
        [Settings.mod_key],
        "l",
        lazy.spawn(Settings.commands.lock),
        desc="Lock the screen",
    ),
    Key(
        [Settings.mod_key],
        "v",
        lazy.spawn(Settings.commands.quicklinks),
        desc="Show quick links",
    ),
    Key([], "XF86AudioRaiseVolume", lazy.function(change_volume, 2)),
    Key([], "XF86AudioLowerVolume", lazy.function(change_volume, -2)),
    Key([], "XF86AudioMute", lazy.function(toggle_mute)),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),
    Key([], "XF86MonBrightnessUp", lazy.function(change_brightness, 2)),
    Key([], "XF86MonBrightnessDown", lazy.function(change_brightness, -2)),
    *(
        Key([Settings.mod_key], f"F{i}", lazy.spawn(f))
        for i, f in enumerate(Settings.favorites, start=1)
    ),
    *[
        group_key
        for (i, g) in enumerate(groups, start=1)
        for group_key in (
            Key(
                [Settings.mod_key],
                str(i),
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            Key(
                [Settings.mod_key, "shift"],
                str(i),
                lazy.window.togroup(g.name, switch_group=True),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
        )
    ],
]
