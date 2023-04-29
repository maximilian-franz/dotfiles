from libqtile.dgroups import simple_key_binder
from modules.constants import COLOR_SCHEME, FONT
from modules.keys import groups, keys
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens
from modules.theme import GruvBox

auto_minimize = False
extension_defaults = dict(
    font=FONT,
    fontsize=16,
    padding=10,
    background=COLOR_SCHEME.background,
    foreground=COLOR_SCHEME.foreground,
)
wmname = "Qtile"
widget_defaults = extension_defaults.copy()
