import pathlib
from .theme import GruvBox

COLOR_SCHEME = GruvBox.Dark
CONFIG_DIR = pathlib.Path.home() / ".config"
FONT = "Hack Nerd Font"
MAX_WINDOW_NAME_COMPONENT_LENGTH = 50
MOD = "mod4"
WALLPAPER = CONFIG_DIR / "wallpapers" / "temple_03.jpeg"
APP_ICONS = {
    "discord": "󰙯",
    "github": "󰊤",
    "gitlab": "󰮠",
    "gmail": "󰊫",
    "google": "󰊭",
    "google-maps": "󰗵",
    "mozilla-firefox": "󰈹",
    "mozilla-thunderbird": "󰇮",
    "reddit": "󰑍",
    "spotify": "󰓇",
    "stack-exchange": "󰘋",
    "stack-overflow": "󰓌",
    "steam": "󰓓",
    "thunar": "󰉋",
    "visual-studio-code": "󰨞",
    "youtube": "󰗃",
}
