import psutil
import re
from .constants import APP_ICONS, MAX_WINDOW_NAME_COMPONENT_LENGTH


def get_icon_for_app(app_name: str):
    return APP_ICONS.get("-".join(app_name.lower().split()), app_name)


def get_network_interface():
    interfaces = list(psutil.net_if_addrs().keys())
    return interfaces[1] if len(interfaces) > 1 else "lo"


def get_unique_values(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def get_shortened_components(components: list[str]):
    if sum(len(c) for c in components) > MAX_WINDOW_NAME_COMPONENT_LENGTH:
        longest_component = max(components[1:], key=len)
        components[components.index(longest_component)] = "..."
        return get_unique_values(get_shortened_components(components))
    return components


def parse_window_name(raw_name: str):
    components = list(reversed(re.split(r"\s+[-־᠆‐‑‒–—―﹘﹣－·]\s+", raw_name)))
    if components[0] == "Mozilla Firefox":
        components = [get_icon_for_app(c) for c in components]
    else:
        components[0] = get_icon_for_app(components[0])
    shortened_components = get_shortened_components(components)
    return "  ".join(shortened_components)
