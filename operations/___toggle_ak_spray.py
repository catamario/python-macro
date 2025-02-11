from console.interface import update_text_color
import threading
import time

from operations._mouse_down import is_mouse_down, is_mouse_down_duck
from data.points import points_lua_duck, points_lua, points_thompson_duck, points_thompson, points_mp5, points_mp5_duck, \
    points_lr300_duck, points_lr300, points_sar_duck, points_sar
import win32api
import win32con
from data.interpolate_points import split_points





import pyautogui
ak_spray_enabled = False
def toggle_ak_spray():
    global ak_spray_enabled, mouse_thread, ongoing
    global text_widget1
    if not ak_spray_enabled:
        ak_spray_enabled = True
        print("AK Spray: ENABLED")
        update_text_color(ak_spray_enabled, text_widget=1)
        cheat_thread = threading.Thread(target=cheat_ak,daemon=True)
        cheat_thread.start()
    else:
        ak_spray_enabled = False
        print("AK Spray: DISABLED")
        update_text_color(ak_spray_enabled, text_widget=1)

thompson_spray_enabled = False
def toggle_thompson_spray():
    global thompson_spray_enabled, mouse_thread, ongoing
    if not thompson_spray_enabled:
        thompson_spray_enabled = True
        print("thompson Spray: ENABLED")
        update_text_color(thompson_spray_enabled, text_widget=2)
        cheat_thread = threading.Thread(target=cheat_thompson,daemon=True)
        cheat_thread.start()
    else:
        thompson_spray_enabled = False
        print("thompson Spray: DISABLED")
        update_text_color(thompson_spray_enabled, text_widget=2)

mp5_spray_enabled = False
def toggle_mp5_spray():
    global mp5_spray_enabled, mouse_thread, ongoing
    if not mp5_spray_enabled:
        mp5_spray_enabled = True
        print("mp5 Spray: ENABLED")
        update_text_color(mp5_spray_enabled, text_widget=3)
        cheat_thread = threading.Thread(target=cheat_mp5,daemon=True)
        cheat_thread.start()
    else:
        mp5_spray_enabled = False
        print("mp5 Spray: DISABLED")
        update_text_color(mp5_spray_enabled, text_widget=3)

lr300_spray_enabled = False
def toggle_lr300_spray():
    global lr300_spray_enabled, mouse_thread, ongoing
    if not lr300_spray_enabled:
        lr300_spray_enabled = True
        print("lr300 Spray: ENABLED")
        update_text_color(lr300_spray_enabled, text_widget=4)
        cheat_thread = threading.Thread(target=cheat_lr300,daemon=True)
        cheat_thread.start()
    else:
        lr300_spray_enabled = False
        print("lr300 Spray: DISABLED")
        update_text_color(lr300_spray_enabled, text_widget=4)

sar_spray_enabled = False
def toggle_sar_spray():
    global sar_spray_enabled, mouse_thread, ongoing
    if not sar_spray_enabled:
        sar_spray_enabled = True
        print("SAR Spray: ENABLED")
        update_text_color(sar_spray_enabled, text_widget=5)
        cheat_thread = threading.Thread(target=cheat_sar,daemon=True)
        cheat_thread.start()
    else:
        sar_spray_enabled = False
        print("SAR Spray: DISABLED")
        update_text_color(sar_spray_enabled, text_widget=5)

import time

def sleep_for(a, b):
    start_time = time.perf_counter()  # Începe măsurarea timpului
    while (time.perf_counter() - start_time) < (a / b): #todo: am modifica din /1000 la /2000 pt ca lua se misca mai rapid
        pass


def reset_index_memory():
    global index_duck_memory, index_memory
    if not is_mouse_down_duck() and not is_mouse_down():
        index_duck_memory = 0
        index_memory = 0

#todo: Odata inceput un spray, se da True ca sa se tina cont cand se intra in celalalt
#todo: Verificare la fiecare spray daca e True celalalt pentru a continua cu un alt i in for
#todo: daca in spray nu se incepe celalalt spray atunci se iese din el la deapasare prin facerea in False a state ului si resetarea indexului memorat

def cheat_ak():
    global index_duck_memory, index_memory
    index_duck_memory=0
    index_memory=0
    while True:
        reset_index_memory()

        if is_mouse_down_duck():
            if index_memory == 0:
                sleep_for(5, 1050)
            for i in range(index_memory, len(points_lua_duck)):
                dx, dy = points_lua_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(34, 1050)
                    sleep_for(3, 1050)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1050)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS

                if i != len(points_lua_duck)-1:
                    index_duck_memory = i
                else:
                    index_duck_memory = 0
                    index_memory = 0

                if is_mouse_down():
                    break

                if not is_mouse_down_duck():
                    index_duck_memory=0
                    break

        reset_index_memory()

        if is_mouse_down():
            if index_duck_memory == 0:
                sleep_for(3, 1130)
            for i in range(index_duck_memory, len(points_lua)):
                dx, dy = points_lua[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(34, 1130)
                    sleep_for(3, 1130)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1130)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS

                if i != len(points_lua) - 1:
                    index_memory = i
                else:
                    index_memory = 0
                    index_duck_memory = 0

                if is_mouse_down_duck():
                    break

                if not is_mouse_down():
                    index_memory=0
                    break

        reset_index_memory()

        if not ak_spray_enabled:
            break



def cheat_thompson():
    global index_duck_memory, index_memory
    index_duck_memory = 0
    index_memory = 0
    while True:
        reset_index_memory()
        if is_mouse_down_duck():
            if index_memory == 0:
                sleep_for(5, 900)
                sleep_for(5, 900)
            for i in range(index_memory, len(points_thompson_duck)):
                dx, dy = points_thompson_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 20 == 0:
                    sleep_for(5, 900)
                    sleep_for(30, 900)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(5, 900)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if i != len(points_thompson_duck)-1:
                    index_duck_memory = i
                else:
                    index_duck_memory = 0
                    index_memory = 0

                if is_mouse_down():
                    break

                if not is_mouse_down_duck():
                    index_duck_memory=0
                    break

        reset_index_memory()
        if is_mouse_down():
            for i in range(index_duck_memory, len(points_thompson)):
                dx, dy = points_thompson[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 20 == 0:
                    sleep_for(5, 950)
                    sleep_for(30, 950)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(5, 950)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if i != len(points_thompson) - 1:
                    index_memory = i
                else:
                    index_memory = 0
                    index_duck_memory = 0

                if is_mouse_down_duck():
                    break

                if not is_mouse_down():
                    index_memory=0
                    break


        reset_index_memory()
        if not thompson_spray_enabled:
            break



def cheat_mp5():
    global index_duck_memory, index_memory
    index_duck_memory = 0
    index_memory = 0
    while True:
        reset_index_memory()
        if is_mouse_down_duck():
            if index_memory == 0:
                sleep_for(5, 1225)
                sleep_for(3, 1225)
            for i in range(index_memory, len(points_mp5_duck)):
                dx, dy = points_mp5_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(1, 1225)
                    sleep_for(3, 1225)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1225)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if i != len(points_mp5_duck)-1:
                    index_duck_memory = i
                else:
                    index_duck_memory = 0
                    index_memory = 0

                if is_mouse_down():
                    break

                if not is_mouse_down_duck():
                    index_duck_memory=0
                    break

        reset_index_memory()
        if is_mouse_down():
            if index_duck_memory == 0:
                sleep_for(5, 1250)
                sleep_for(3, 1250)
            for i in range(index_duck_memory, len(points_mp5)):
                dx, dy = points_mp5[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(1, 1250)
                    sleep_for(3, 1250)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1250)
                    #sleep_for(3, 1250)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if i != len(points_mp5) - 1:
                    index_memory = i
                else:
                    index_memory = 0
                    index_duck_memory = 0

                if is_mouse_down_duck():
                    break

                if not is_mouse_down():
                    index_memory=0
                    break


        reset_index_memory()
        if not mp5_spray_enabled:
            break





def cheat_lr300():
    global index_duck_memory, index_memory
    index_duck_memory = 0
    index_memory = 0
    while True:
        reset_index_memory()
        if is_mouse_down_duck():
            if index_memory == 0:
                sleep_for(3, 1000)
            for i in range(index_memory, len(points_lr300_duck)):
                dx, dy = points_lr300_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(21, 1000)
                    sleep_for(3, 1000)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1000)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if i != len(points_lr300_duck)-1:
                    index_duck_memory = i
                else:
                    index_duck_memory = 0
                    index_memory = 0

                if is_mouse_down():
                    break

                if not is_mouse_down_duck():
                    index_duck_memory=0
                    break

        reset_index_memory()
        if is_mouse_down():
            b=1100
            if index_duck_memory == 0:
                sleep_for(3, b)
                sleep_for(3, b)
            for i in range(index_duck_memory, len(points_lr300)):
                dx, dy = points_lr300[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(21, b)
                    sleep_for(3, b)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, b)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if i != len(points_lr300) - 1:
                    index_memory = i
                else:
                    index_memory = 0
                    index_duck_memory = 0

                if is_mouse_down_duck():
                    break

                if not is_mouse_down():
                    index_memory=0
                    break

        reset_index_memory()

        if not lr300_spray_enabled:
            break





def cheat_sar():
    while True:
        if is_mouse_down_duck():
            sleep_for(1, 1000)
            for i in range(0, len(points_sar_duck)):
                dx, dy = points_sar_duck[i]
                dx=int(dx*2.2)
                dy=int(dy*2.2)
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                sleep_for(5, 950)
                if not is_mouse_down_duck():
                    break

        elif is_mouse_down():
            sleep_for(1, 1000)
            for i in range(0, len(points_sar)):
                dx, dy = points_sar[i]
                dx=int(dx*3.7)
                dy=int(dy*3.7)
                #2.9 era inainte
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                sleep_for(5, 950)
                if not is_mouse_down():
                    break


        if not sar_spray_enabled:
            break

