from libqtile import bar, widget
from .constants import COLOR_SCHEME, FONT
from .utils import parse_window_name

top_bar = bar.Bar(
    [
        widget.GroupBox(
            active=COLOR_SCHEME.foreground,
            block_highlight_text_color=COLOR_SCHEME.background,
            highlight_method="block",
            inactive=COLOR_SCHEME.foreground_4,
            rounded=False,
            this_current_screen_border=COLOR_SCHEME.green_hard,
            this_screen_border=COLOR_SCHEME.background_2,
            padding=5,
        ),
        widget.WindowName(parse_text=parse_window_name),
        widget.Chord(),
        widget.Systray(background=COLOR_SCHEME.background_soft, padding=10),
        widget.Spacer(length=5, background=COLOR_SCHEME.background_soft),
        widget.Memory(
            background=COLOR_SCHEME.background_1,
            format="󰍛 {MemPercent}%",
        ),
        widget.CPU(
            background=COLOR_SCHEME.background_2,
            format="󰻠 {load_percent}%",
        ),
        widget.Wttr(
            format="%t %C",
            location={"Potsdam": "Potsdam"},
            background=COLOR_SCHEME.background_3,
        ),
        widget.Clock(
            font=FONT + " bold",
            format="%H:%M:%S",
            background=COLOR_SCHEME.green_hard,
            foreground=COLOR_SCHEME.background_1,
        ),
    ],
    24,
    background=COLOR_SCHEME.background,
)
