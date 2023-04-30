import alsaaudio
import dbus
import re
from Xlib import display as xdisplay
from .settings import Settings

session_bus = dbus.SessionBus()


# General Utils


def get_character_bar(value: int, max_length: int = 20):
    return "━" * round(value * max_length)


def get_number_of_screens():
    num_screens = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_screens += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_screens


def get_unique_values(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def send_notification(
    message: str,
    app: str | None = None,
    urgency: int = 1,
    icon_name: str | None = None,
    expiration_timeout: int = 500,
):
    notify_name = "org.freedesktop.Notifications"
    notify_path = "/org/freedesktop/Notifications"
    notify_object = session_bus.get_object(notify_name, notify_path)
    notify_interface = dbus.Interface(notify_object, notify_name)
    hints = {"urgency": urgency}
    if app is not None:
        hints |= {"x-dunst-stack-tag": app}
    notify_interface.Notify(
        app, 0, icon_name, message, "", [], hints, expiration_timeout
    )


# Window Name Parsing


def get_icon_for_app(app_name: str):
    return Settings.icons.get("-".join(app_name.lower().split()), app_name)


def get_shortened_components(components: list[str]):
    if sum(len(c) for c in components) > Settings.max_window_name_component_length:
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


# Volume Control


def get_volume_icon(volume: int, mute: bool):
    if mute:
        return "notification-audio-volume-muted"
    if volume == 0:
        return "notification-audio-volume-off"
    if volume <= 33:
        return "notification-audio-volume-low"
    if volume <= 67:
        return "notification-audio-volume-medium"
    return "notification-audio-volume-high"


def get_volume_bar(volume: int):
    return get_character_bar(volume / 100)


def change_volume(qtile, delta: int):
    mixer = alsaaudio.Mixer("Master")
    if sum(mixer.getmute()) > 0:
        mixer.setmute(0)
    new_volume = max(0, min(mixer.getvolume()[0] + delta, 100))
    mixer.setvolume(new_volume)
    send_notification(
        get_volume_bar(new_volume),
        app="changeVolume",
        icon_name=get_volume_icon(new_volume, False),
    )


def toggle_mute(qtile):
    mixer = alsaaudio.Mixer("Master")
    if sum(mixer.getmute()) > 0:
        mixer.setmute(0)
        volume = mixer.getvolume()[0]
        send_notification(
            get_volume_bar(volume),
            app="changeBrightness",
            icon_name=get_volume_icon(volume, False),
        )
    else:
        mixer.setmute(1)
        send_notification(
            "", app="changeBrightness", icon_name=get_volume_icon(0, True)
        )


# Brightness Control


def get_brightness_icon(brightness: float):
    if brightness == 1.0:
        return "notification-display-brightness-full"
    if brightness < 0.33:
        return "notification-display-brightness-low"
    if brightness < 0.66:
        return "notification-display-brightness-medium"
    return "notification-display-brightness-high"


def get_brightness_bar(brightness: float):
    return get_character_bar(brightness)


def change_brightness(qtile, delta: int):
    clight_name = "org.clight.clight"
    clight_path = "/org/clight/clight"

    clight_object = session_bus.get_object(clight_name, clight_path)
    clight_interface = dbus.Interface(clight_object, dbus.PROPERTIES_IFACE)

    if delta < 0:
        clight_object.DecBl(-delta / 100, dbus_interface=clight_name)
    else:
        clight_object.IncBl(delta / 100, dbus_interface=clight_name)

    brightness = round(clight_interface.Get(clight_name, "BlPct"), 2)
    send_notification(
        get_brightness_bar(brightness),
        app="changeBrightness",
        icon_name=get_brightness_icon(brightness),
    )
