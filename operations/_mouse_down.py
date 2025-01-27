import time
import win32api

def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    rmb_state = win32api.GetKeyState(0x02)
    return lmb_state < 0 and rmb_state < 0

if __name__ == "__main__":
    while True:
        print(f"{is_mouse_down()}")
        time.sleep(2)