from pynput import keyboard
from operations._toggle_ak_spray import toggle_ak_spray


def on_press(key):
    if key == keyboard.Key.f2:
        toggle_ak_spray()


def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()