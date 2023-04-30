from libqtile import bar, widget
from .settings import Settings
from .utils import parse_window_name

top_bar = bar.Bar(
    [
        widget.GroupBox(
            active=Settings.theme.colors.foreground,
            block_highlight_text_color=Settings.theme.colors.background,
            highlight_method="block",
            inactive=Settings.theme.colors.foreground_4,
            rounded=False,
            this_current_screen_border=Settings.theme.colors.green_hard,
            this_screen_border=Settings.theme.colors.background_2,
            padding=5,
        ),
        widget.WindowName(parse_text=parse_window_name),
        widget.Chord(),
        widget.Systray(background=Settings.theme.colors.background_soft, padding=10),
        widget.Spacer(length=5, background=Settings.theme.colors.background_soft),
        widget.Memory(
            background=Settings.theme.colors.background_1,
            format="󰍛 {MemPercent}%",
        ),
        widget.CPU(
            background=Settings.theme.colors.background_2,
            format="󰻠 {load_percent}%",
        ),
        widget.Wttr(
            format="%t %C",
            location={"Potsdam": "Potsdam"},
            background=Settings.theme.colors.background_3,
        ),
        widget.Clock(
            font=Settings.theme.font + " bold",
            format="󰃭 %a %m/%d 󰥔 %H:%M:%S",
            background=Settings.theme.colors.green_hard,
            foreground=Settings.theme.colors.background_1,
        ),
    ],
    24,
    background=Settings.theme.colors.background,
)
