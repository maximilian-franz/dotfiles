from libqtile import layout
from libqtile.config import Match
from .constants import COLOR_SCHEME

layouts = [
    layout.Columns(
        border_width=1,
        border_focus=COLOR_SCHEME.green_hard,
        border_normal=COLOR_SCHEME.background_soft,
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
