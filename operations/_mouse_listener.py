from pynput import mouse
from operations.cheat import cheat

mouse_listener = None
def start_mouse_listener():
    global mouse_listener
    if mouse_listener is None:
        mouse_listener = mouse.Listener(on_click=cheat)
        mouse_listener.start()


def stop_mouse_listener():
    global mouse_listener
    if mouse_listener is not None:
        mouse_listener.stop()
        mouse_listener = None
