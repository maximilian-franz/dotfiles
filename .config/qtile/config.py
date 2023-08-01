import importlib
import sys
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


def reload(module):
    if module in sys.modules:
        importlib.reload(sys.modules[module])


reload("moduels.settings")
from modules.settings import Settings

reload("modules.utils")
from modules.utils import (
    change_brightness,
    change_volume,
    get_number_of_screens,
    parse_window_name,
    toggle_mute,
)

auto_minimize = False
extension_defaults = dict(
    font=Settings.font,
    fontsize=16,
    padding=10,
    background=Settings.colors.background,
    foreground=Settings.colors.foreground,
)
wmname = "Qtile"
widget_defaults = extension_defaults.copy()

# Widgets

my_widgets = [
    widget.GroupBox(
        active=Settings.colors.foreground,
        block_highlight_text_color=Settings.colors.background,
        highlight_method="block",
        inactive=Settings.colors.foreground_4,
        rounded=False,
        this_current_screen_border=Settings.colors.green_hard,
        this_screen_border=Settings.colors.background_2,
        padding=5,
    ),
    widget.WindowName(parse_text=parse_window_name),
    widget.Chord(),
    widget.Systray(background=Settings.colors.background, padding=10),
    widget.Spacer(length=5, background=Settings.colors.background),
    widget.KeyboardLayout(
        background=Settings.colors.background_2,
        configured_keyboards=["de", "us intl"],
        fmt="󰌌 {}",
    ),
    widget.Memory(
        background=Settings.colors.background_3,
        format="󰍛 {MemPercent}%",
    ),
    widget.CPU(
        background=Settings.colors.background_4,
        format="󰻠 {load_percent}%",
    ),
    widget.Clock(
        font=Settings.font + " bold",
        format="󰃭 %a %m/%d 󰥔 %H:%M:%S",
        background=Settings.colors.green_hard,
        foreground=Settings.colors.background_1,
    ),
]
my_bar = bar.Bar(
    my_widgets, 24, background=f"{Settings.colors.background}.0", opacity=1.0
)

# Screens

screens = [
    Screen(top=my_bar, wallpaper=Settings.wallpaper, wallpaper_mode="fill"),
    *(
        Screen(wallpaper=Settings.wallpaper, wallpaper_mode="fill")
        for _ in range(1, get_number_of_screens())
    ),
]

# Mouse

mouse = [
    Drag(
        [Settings.mod_key],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [Settings.mod_key],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    Click([Settings.mod_key], "Button2", lazy.window.bring_to_front()),
]

# Layouts

layouts = [
    layout.Columns(
        border_width=1,
        border_focus=Settings.colors.green_hard,
        border_normal=Settings.colors.background_soft,
        margin=10,
        margin_on_single=0,
    ),
    layout.Max(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="blueman-manager"),  # blueman-manager
        Match(wm_class="pavucontrol"),  # pavucontrol
        Match(wm_class="feh"),  # feh
        Match(wm_class="gnome-calculator"),  # gnome-calculator
        Match(wm_class="Steam", title="Friends List"),  # Steam Friends List
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=0,
    border_focus="#000000",
    border_normal="#000000",
)

# Keys

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
        mode=True,
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
        mode=True,
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
