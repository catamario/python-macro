from operations._mouse_down import is_mouse_down
import time

from operations.path_recorder import left_pressed


def cheat(x, y, button, pressed):
    while True:
        if is_mouse_down():
            print("CACA")
        time.sleep(1)



    """
    Mută cursorul în pași mici de la (start_x, start_y) la (end_x, end_y).
    """
#TODO:    dx = (end_x - start_x) / SMOOTH_STEPS
#TODO:    dy = (end_y - start_y) / SMOOTH_STEPS
if __name__ == "__main__":
    cheat(1, 1 , left_pressed, True)


