import pathlib
from .theme import GruvBox

COLOR_SCHEME = GruvBox.Dark
CONFIG_DIR = pathlib.Path.home() / ".config"
FAVORITES = ["firefox", "thunar", "code", "thunderbird"]
FONT = "Hack Nerd Font"
GROUPS = "123456789"
LAUNCHER_CMD = str(CONFIG_DIR / "rofi" / "scripts" / "launcher_t3")
LOCK_CMD = "betterlockscreen -l"
MAX_WINDOW_NAME_COMPONENT_LENGTH = 50
MOD = "mod4"
POWER_MENU_CMD = str(CONFIG_DIR / "rofi" / "scripts" / "powermenu_t4")
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
