import pyautogui
from pynput import mouse

# Variabile pentru a urmări statusul butoanelor
left_pressed = False
right_pressed = False

# Funcția care se va apela când un buton este apăsat
def cheat(x, y, button, pressed):
    if button == mouse.Button.left and pressed:  # Verificăm dacă a fost apăsat butonul stâng
        print(f'{x}, {y}')

def path_recorder():
    # Start listener pentru a asculta clickurile
    with mouse.Listener(on_click=cheat) as listener:
        listener.join()

if __name__ == "__main__":
    path_recorder()
