from console.interface import update_text_color
from operations._mouse_listener import stop_mouse_listener, start_mouse_listener
import threading


ak_spray_enabled = False
def toggle_ak_spray():
    global ak_spray_enabled, mouse_thread

    if not ak_spray_enabled:
        ak_spray_enabled = True
        print("AK Spray: ENABLED")
        update_text_color(ak_spray_enabled)
        mouse_thread = threading.Thread(target=start_mouse_listener, daemon=True)
        mouse_thread.start()
    else:
        ak_spray_enabled = False
        print("AK Spray: DISABLED")
        update_text_color(ak_spray_enabled)
        stop_mouse_listener()