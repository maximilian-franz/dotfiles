from libqtile.config import Screen
from .settings import Settings
from .utils import get_number_of_screens
from .widgets import *

screens = [
    Screen(top=top_bar, wallpaper=Settings.theme.wallpaper, wallpaper_mode="fill"),
    *(
        Screen(wallpaper=Settings.theme.wallpaper, wallpaper_mode="fill")
        for _ in range(1, get_number_of_screens())
    ),
]
