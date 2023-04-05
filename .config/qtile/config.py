from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget import decorations
from Xlib import display as xdisplay
from theme import GruvBox


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


mod = "mod4"
num_monitors = get_num_monitors()
terminal = guess_terminal()
favorites = ["firefox", "thunar", "code", "thunderbird"]

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
    Key([mod], "o", lazy.next_layout(), desc="Toggle between layouts"),
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
        "XF86AudioPrev",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
            "/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous"
        ),
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
            "/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next"
        ),
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
            "/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"
        ),
    ),
    Key(
        [],
        "XF86AudioStop",
        lazy.spawn(
            "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify "
            "/org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Stop"
        ),
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
        desc="Spawn an application using rofi",
    ),
    Key(
        [mod],
        "Tab",
        lazy.spawn(
            "rofi -modi window -show window -config ~/.config/rofi/rofidmenu.rasi"
        ),
        desc="Spawn an application using rofi",
    ),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn(
            "rofi -show power-menu -modi power-menu:~/.config/rofi/rofi-power-menu -config ~/.config/rofi/powermenu.rasi"
        ),
        desc="Spawn a power menu using rofi",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.spawn("/home/max/.config/i3/scripts/blur-lock"),
        desc="Lock the screen",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("/home/max/.config/i3/scripts/power-profiles"),
        desc="Switch power profiles using rofi",
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
    font="Hack Nerd Font",
    fontsize=14,
    foreground=GruvBox.foreground,
    background=GruvBox.background,
    center_aligned=True,
    theme_path="/usr/share/icons/gruvbox-plus/panel/24/",
)
extension_defaults = widget_defaults.copy()

decorations = {"decorations": [decorations.PowerLineDecoration(path="forward_slash")]}

screens = [
    Screen(
        wallpaper="~/.config/wallpapers/temple_03.jpeg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    this_current_screen_border=GruvBox.background_4,
                    this_screen_border=GruvBox.background_2,
                    active=GruvBox.foreground,
                    inactive=GruvBox.foreground_4,
                    highlight_method="block",
                    rounded=False,
                    **decorations,
                ),
                widget.WindowName(**decorations),
                widget.KeyboardLayout(
                    background=GruvBox.background_2,
                    configured_keyboards=["de", "us intl"],
                ),
                widget.Systray(background=GruvBox.background_2, **decorations),
                widget.Wttr(
                    format="%t %C",
                    background=GruvBox.background_1,
                    location={"Potsdam": "Potsdam"},
                    **decorations,
                ),
                widget.Clock(
                    format="%H:%M",
                    background=GruvBox.background_soft,
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
                wallpaper="~/.config/wallpapers/temple_03.jpeg",
                wallpaper_mode="fill",
            )
        ]
        * (num_monitors - 1)
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
