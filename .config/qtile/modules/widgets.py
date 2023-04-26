from libqtile import bar, widget
from .theme import GruvBox
from .utils import parse_window_name, get_network_interface

top_bar = bar.Bar(
    [
        widget.GroupBox(
            active=GruvBox.foreground,
            block_highlight_text_color=GruvBox.background,
            highlight_method="block",
            inactive=GruvBox.foreground_4,
            rounded=False,
            this_current_screen_border=GruvBox.green_hard,
            this_screen_border=GruvBox.background_2,
            padding=3,
        ),
        widget.Sep(),
        widget.WindowName(parse_text=parse_window_name),
        widget.Sep(),
        widget.Systray(),
        widget.Wttr(
            format="%t %C",
            location={"Potsdam": "Potsdam"},
            background=GruvBox.aqua_hard,
            foreground=GruvBox.background,
        ),
        widget.Clock(
            format="%H:%M:%S",
            background=GruvBox.green_hard,
            foreground=GruvBox.background,
        ),
    ],
    24,
    background=GruvBox.background,
)
