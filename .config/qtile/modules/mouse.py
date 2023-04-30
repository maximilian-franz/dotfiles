from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from .settings import Settings

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
