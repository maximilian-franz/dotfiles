from libqtile.config import Screen
from .constants import WALLPAPER
from .widgets import *

screens = [Screen(top=top_bar, wallpaper=WALLPAPER, wallpaper_mode="fill")]
