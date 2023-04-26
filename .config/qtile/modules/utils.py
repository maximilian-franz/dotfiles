import psutil
import re
from .constants import APP_ICONS


def get_icon_for_app(app_name: str):
    return APP_ICONS.get("-".join(app_name.lower().split()), app_name)


def get_network_interface():
    interfaces = list(psutil.net_if_addrs().keys())
    return interfaces[1] if len(interfaces) > 1 else "lo"


def parse_window_name(raw_name: str):
    components = re.split(r"\s+[-־᠆‐‑‒–—―﹘﹣－·]\s+", raw_name)
    if components[-1] == "Mozilla Firefox":
        components = [get_icon_for_app(c) for c in components]
    else:
        components[-1] = get_icon_for_app(components[-1])
    shortened_components = [(c if len(c) <= 20 else c[:17] + "...") for c in components]
    return "  ".join(reversed(shortened_components))
