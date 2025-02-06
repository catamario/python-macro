import pyautogui
from pynput import mouse
import time
from operations._mouse_down import is_mouse_down
# Variabile pentru a urmări statusul butoanelor

# Funcția care se va apela când un buton este apăsat
def cheat():
    while True:
        if is_mouse_down():
            while True:
                x, y = pyautogui.position()
                print(f'({x}, {y}),')
                time.sleep(0.0000133)
                if not is_mouse_down():
                    break

if __name__ == "__main__":
    cheat()
