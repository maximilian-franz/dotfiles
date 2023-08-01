import pathlib

CONFIG_DIR = pathlib.Path.home() / ".config"


class Gruvbox:
    """Gruvbox Color Scheme"""

    class Dark:
        """Gruvbox Color Scheme Dark Variant"""

        background = "#282828"
        background_hard = "#1D2021"
        background_soft = "#32302F"
        background_1 = "#3C3836"
        background_2 = "#504945"
        background_3 = "#665C54"
        background_4 = "#7C6F64"
        foreground = "#FBF1C7"
        foreground_1 = "#EBDBB2"
        foreground_2 = "#D5C4A1"
        foreground_3 = "#BDAE93"
        foreground_4 = "#A89984"
        red_hard = "#CC241D"
        red_soft = "#FB4934"
        green_hard = "#98971A"
        green_soft = "#B8BB26"
        yellow_hard = "#D79921"
        yellow_soft = "#FABD2F"
        blue_hard = "#458588"
        blue_soft = "#83A598"
        purple_hard = "#B16286"
        purple_soft = "#D3869B"
        aqua_hard = "#689D6A"
        aqua_soft = "#8EC07C"
        orange_hard = "#D65D0E"
        orange_soft = "#FE8019"

    class Light:
        """Gruvbox Color Scheme Light Variant"""

        background = "#FBF1C7"
        background_hard = "#F9F5D7"
        background_soft = "#F2E5BC"
        background_1 = "#EBDBB2"
        background_2 = "#D5C4A1"
        background_3 = "#BDAE93"
        background_4 = "#A89984"
        foreground = "#282828"
        foreground_1 = "#3C3836"
        foreground_2 = "#504945"
        foreground_3 = "#665C54"
        foreground_4 = "#7C6F64"
        red_hard = "#CC241D"
        red_soft = "#9D0006"
        green_hard = "#98971A"
        green_soft = "#79740E"
        yellow_hard = "#D79921"
        yellow_soft = "#B57614"
        blue_hard = "#458588"
        blue_soft = "#076678"
        purple_hard = "#B16286"
        purple_soft = "#8F3F71"
        aqua_hard = "#689D6A"
        aqua_soft = "#427B58"
        orange_hard = "#D65D0E"
        orange_soft = "#AF3A03"


class Commands:
    """Custom Command Settings"""

    launcher = str(CONFIG_DIR / "rofi" / "scripts" / "launcher_t4")
    lock = "betterlockscreen -l"
    power_menu = str(CONFIG_DIR / "rofi" / "scripts" / "powermenu_t4")
    quicklinks = str(CONFIG_DIR / "rofi" / "applets" / "bin" / "quicklinks.sh")


class Settings:
    """Settings"""

    colors = Gruvbox.Dark
    commands = Commands
    favorites = ["firefox", "thunar", "code", "thunderbird"]
    font = "Hack Nerd Font"
    groups = "123456789"
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
    max_window_name_component_length = 50
    mod_key = "mod4"
    wallpaper = CONFIG_DIR / "wallpapers" / "gruvbox_anime-gruv-dark.png"
