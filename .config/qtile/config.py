from libqtile.dgroups import simple_key_binder
from modules.settings import Settings
from modules.keys import groups, keys
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens

auto_minimize = False
extension_defaults = dict(
    font=Settings.theme.font,
    fontsize=16,
    padding=10,
    background=Settings.theme.colors.background,
    foreground=Settings.theme.colors.foreground,
)
wmname = "Qtile"
widget_defaults = extension_defaults.copy()
