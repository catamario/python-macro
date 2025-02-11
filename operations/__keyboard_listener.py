from pynput import keyboard
from operations.___toggle_ak_spray import toggle_ak_spray, toggle_thompson_spray, toggle_mp5_spray, toggle_lr300_spray, \
    toggle_sar_spray

is_enabled_ak=False
is_enabled_thompson=False
is_enabled_mp5=False
is_enabled_lr300=False
is_enabled_sar=False
def on_press(key):
    global is_enabled_ak, is_enabled_thompson, is_enabled_mp5, is_enabled_lr300, is_enabled_sar


    if key == keyboard.Key.f2 and not any([is_enabled_ak, is_enabled_thompson, is_enabled_mp5, is_enabled_lr300, is_enabled_sar]):
        toggle_ak_spray()
        is_enabled_ak = True  # Setează ca activat


    elif key == keyboard.Key.f2 and is_enabled_ak == True and not any([is_enabled_thompson, is_enabled_mp5, is_enabled_lr300, is_enabled_sar]):
        toggle_ak_spray()
        is_enabled_ak = False  # Setează ca activat

    elif key == keyboard.Key.f3 and not any([is_enabled_ak, is_enabled_thompson, is_enabled_mp5, is_enabled_lr300, is_enabled_sar]):
        toggle_thompson_spray()
        is_enabled_thompson = True  # Setează ca activat

    elif key == keyboard.Key.f3 and is_enabled_thompson == True and not any([is_enabled_ak, is_enabled_mp5, is_enabled_lr300, is_enabled_sar]):
        toggle_thompson_spray()
        is_enabled_thompson = False  # Setează ca activat

    elif key == keyboard.Key.f4 and not any([is_enabled_ak, is_enabled_thompson, is_enabled_lr300, is_enabled_mp5, is_enabled_sar]):
        toggle_mp5_spray()
        is_enabled_mp5 = True  # Setează ca activat

    elif key == keyboard.Key.f4 and is_enabled_mp5 == True and not any([is_enabled_thompson, is_enabled_ak, is_enabled_lr300, is_enabled_sar]):
        toggle_mp5_spray()
        is_enabled_mp5 = False  # Setează ca activat

    elif key == keyboard.Key.f5 and not any([is_enabled_ak, is_enabled_thompson, is_enabled_lr300, is_enabled_mp5, is_enabled_sar]):
        toggle_lr300_spray()
        is_enabled_lr300 = True  # Setează ca activat

    elif key == keyboard.Key.f5 and is_enabled_lr300 == True and not any([is_enabled_thompson, is_enabled_ak, is_enabled_mp5, is_enabled_sar]):
        toggle_lr300_spray()
        is_enabled_lr300 = False  # Setează ca activat

    elif key == keyboard.Key.f6 and not any([is_enabled_ak, is_enabled_thompson, is_enabled_lr300, is_enabled_mp5, is_enabled_sar]):
        toggle_sar_spray()
        is_enabled_sar = True  # Setează ca activat

    elif key == keyboard.Key.f6 and is_enabled_sar == True and not any([is_enabled_thompson, is_enabled_ak, is_enabled_mp5, is_enabled_lr300]):
        toggle_sar_spray()
        is_enabled_sar = False  # Setează ca activat


def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()