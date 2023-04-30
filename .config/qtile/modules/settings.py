import pathlib
from .color_schemes import GruvBox

CONFIG_DIR = pathlib.Path.home() / ".config"


class Commands:
    """Custom Command Settings"""

    launcher = str(CONFIG_DIR / "rofi" / "scripts" / "launcher_t3")
    lock = "betterlockscreen -l"
    power_menu = str(CONFIG_DIR / "rofi" / "scripts" / "powermenu_t4")
    quicklinks = str(CONFIG_DIR / "rofi" / "applets" / "bin" / "quicklinks.sh")


class Theme:
    """Theme Settings"""

    font = "Hack Nerd Font"
    icons = {
        "discord": "󰙯",
        "github": "󰊤",
        "gitlab": "󰮠",
        "gmail": "󰊫",
        "google": "󰊭",
        "google-maps": "󰗵",
        "keepassxc": "󰌋",
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


class Dark(Theme):
    """Dark Theme Settings"""

    colors = GruvBox.Dark
    wallpaper = CONFIG_DIR / "wallpapers" / "gruvbox_anime-gruv-dark.png"


class Light(Theme):
    """Light Theme Settings"""

    colors = GruvBox.Light
    wallpaper = CONFIG_DIR / "wallpapers" / "gruvbox_anime-gruv-light.png"


class Settings:
    """Settings"""

    commands = Commands
    favorites = ["firefox", "thunar", "code", "thunderbird"]
    groups = "123456789"
    max_window_name_component_length = 50
    mod_key = "mod4"
    theme = Dark
