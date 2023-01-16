from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget import decorations
from Xlib import display as xdisplay
from theme import GruvBox
from dataclasses import dataclass, field
import subprocess


@dataclass
class ThemeColors:
    primary: str
    secondary: str
    tertiary: str
    foreground: str = GruvBox.foreground
    background: str = GruvBox.background


@dataclass
class Theme:
    wallpaper: str
    accent_colors: ThemeColors
    secondary_wallpaper: str | None = None
    apps: list[list[str]] = field(default_factory=list)

    def __post_init__(self):
        if not self.secondary_wallpaper:
            self.secondary_wallpaper = self.wallpaper


heart_skull = Theme(
    wallpaper="~/.config/wallpapers/gruvbox13.png",
    accent_colors=ThemeColors(
        GruvBox.blue_hard, GruvBox.aqua_hard, GruvBox.purple_hard
    ),
    secondary_wallpaper="~/.config/wallpapers/gruvbox27.png",
    apps=[["conky", "-c", "/home/max/.config/conky/hear_skull.conf", "-d"]],
)

minimal = Theme(
    wallpaper="~/.config/wallpapers/gruvbox27.png",
    accent_colors=ThemeColors(
        GruvBox.background_1,
        GruvBox.background_2,
        GruvBox.background_3,
        GruvBox.foreground_4,
    ),
    apps=[["conky", "-c", "/home/max/.config/conky/minimal.conf", "-d"]],
)

CURRENT_THEME = minimal
mod = "mod4"


def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors


@hook.subscribe.startup
def start_theme_apps():
    for app in CURRENT_THEME.apps:
        subprocess.Popen(app)


num_monitors = get_num_monitors()
terminal = guess_terminal()
favorites = ["firefox", "thunar", "code"]

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("/home/max/.config/qtile/scripts/changeVolume up"),
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("/home/max/.config/qtile/scripts/changeVolume down"),
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("/home/max/.config/qtile/scripts/changeVolume mute"),
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("/home/max/.config/qtile/scripts/changeBrightness up"),
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("/home/max/.config/qtile/scripts/changeBrightness down"),
    ),
    Key(
        [mod],
        "d",
        lazy.spawn(
            "rofi -modi drun -show drun -show-icons -config ~/.config/rofi/rofidmenu.rasi"
        ),
        desc="Spawn a command using rofi",
    ),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn(
            "rofi -show power-menu -modi power-menu:~/.config/rofi/rofi-power-menu -config ~/.config/rofi/powermenu.rasi"
        ),
        desc="Spawn a power menu using rofi",
    ),
]

keys.extend(
    [
        Key([mod], f"F{index}", lazy.spawn(command))
        for index, command in enumerate(favorites, start=1)
    ]
)

groups = [Group(i) for i in "123456789"]

for group in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                group.name,
                lazy.group[group.name].toscreen(),
                desc=f"Switch to group {group.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                group.name,
                lazy.window.togroup(group.name, switch_group=True),
                desc=f"Switch to & move focused window to group {group.name}",
            ),
        ]
    )

layouts = [
    layout.Columns(
        border_focus=GruvBox.background_4,
        border_normal=GruvBox.background_soft,
        margin=4,
        margin_on_single=0,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=14,
    foreground=CURRENT_THEME.accent_colors.foreground,
    background=CURRENT_THEME.accent_colors.background,
    center_aligned=True,
    theme_path="/usr/share/icons/Gruvbox_Dark/panel/24/",
)
extension_defaults = widget_defaults.copy()

decorations = {"decorations": [decorations.PowerLineDecoration(path="forward_slash")]}

screens = [
    Screen(
        wallpaper=CURRENT_THEME.wallpaper,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    this_current_screen_border=CURRENT_THEME.accent_colors.tertiary,
                    active=CURRENT_THEME.accent_colors.foreground,
                    inactive=CURRENT_THEME.accent_colors.secondary,
                    highlight_method="block",
                    rounded=False,
                    **decorations,
                ),
                widget.Spacer(**decorations),
                widget.WindowName(),
                widget.Spacer(**decorations),
                widget.KeyboardLayout(
                    background=CURRENT_THEME.accent_colors.primary,
                    configured_keyboards=["de", "us"],
                ),
                widget.Volume(
                    background=CURRENT_THEME.accent_colors.primary,
                    volume_app="pavucontrol",
                    update_interval=0.2,
                ),
                widget.Systray(
                    background=CURRENT_THEME.accent_colors.primary, **decorations
                ),
                widget.Wttr(
                    format="%t %c",
                    background=CURRENT_THEME.accent_colors.secondary,
                    location={"Potsdam": "Potsdam"},
                    **decorations,
                ),
                widget.Clock(
                    format="%H:%M",
                    background=CURRENT_THEME.accent_colors.tertiary,
                ),
            ],
            24,
        ),
    ),
]

if num_monitors > 1:
    screens.extend(
        [
            Screen(
                wallpaper=CURRENT_THEME.secondary_wallpaper,
                wallpaper_mode="fill",
            )
            for _ in range(num_monitors - 1)
        ]
    )

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_width=0,
    border_focus="#000000",
    border_normal="#000000",
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
