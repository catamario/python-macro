import threading
from pynput import keyboard, mouse
import pyautogui as pag
import time

from console.interface import update_text_color

mouse_thread = None
ak_spray_enabled = False

left_pressed = False
right_pressed = False
mouse_listener = None  # Variabilă globală pentru a opri listener-ul mouse

points = [
    (968, 207),
    (968, 219),
    (963, 247),
    (953, 269),
    (945, 285),
    (923, 312),
    (919, 332),
    (902, 345),
    (888, 374),
    (889, 387),
    (865, 415),
    (858, 429),
    (834, 455),
    (830, 478),
    (831, 495),
    (831, 520),
    (831, 536),
    (810, 561),
    (799, 578),
    (796, 601),
    (765, 623),
    (763, 644),
    (762, 665),
    (763, 682),
    (739, 706),
    (730, 725),
    (706, 749),
    (705, 767),
    (705, 790),
    (706, 807)
]


def cheat(x, y, button, pressed):
    global left_pressed, right_pressed, ak_spray_enabled

    if button == mouse.Button.left:
        left_pressed = pressed

    if button == mouse.Button.right:
        right_pressed = pressed

    if left_pressed and right_pressed and ak_spray_enabled:
        current_x, current_y = pag.position()  # Poziția curentă a mouse-ului

        # Parcurge lista de puncte și mișcă mouse-ul relativ
        for i in range(1, len(points)):  # Începem de la al doilea punct (index 1)
            prev_point = points[i - 1]
            point = points[i]

            # Calculează diferențele față de punctul precedent
            dx = point[0] - prev_point[0]
            dy = point[1] - prev_point[1]

            # Mișcă mouse-ul relativ față de poziția curentă
            pag.moveRel(dx, dy)

        left_pressed = False
        right_pressed = False


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


def on_press(key):
    if key == keyboard.Key.f2:
        toggle_ak_spray()


def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
