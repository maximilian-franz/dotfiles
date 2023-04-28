from libqtile.config import Screen
from .constants import WALLPAPER
from .utils import get_number_of_screens
from .widgets import *

screens = [
    Screen(top=top_bar, wallpaper=WALLPAPER, wallpaper_mode="fill"),
    *(Screen(wallpaper=WALLPAPER, wallpaper_mode="fill") for _ in range(1, get_number_of_screens()))
]
