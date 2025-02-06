from console.interface import update_text_color
import threading
import time

from operations._mouse_down import is_mouse_down, is_mouse_down_duck
from data.points import points_lua_duck, points_lua, points_thompson_duck, points_thompson, points_mp5, points_mp5_duck, \
    points_lr300_duck, points_lr300
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

import time

def sleep_for(a, b):
    start_time = time.perf_counter()  # Începe măsurarea timpului
    while (time.perf_counter() - start_time) < (a / b): #todo: am modifica din /1000 la /2000 pt ca lua se misca mai rapid
        pass

def cheat_ak():
    while True:
        if is_mouse_down_duck():
            sleep_for(3, 1050)
            for i in range(0, len(points_lua_duck)):
                dx, dy = points_lua_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(34, 1050)
                    sleep_for(3, 1050)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1050)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down_duck():
                    break

        elif is_mouse_down():
            sleep_for(3, 1130)
            for i in range(0, len(points_lua)):
                dx, dy = points_lua[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(34, 1130)
                    sleep_for(3, 1130)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1130)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down():
                    break


        if not ak_spray_enabled:
            break



def cheat_thompson():
    while True:
        if is_mouse_down_duck():
            sleep_for(5, 900)
            sleep_for(5, 900)
            for i in range(0, len(points_thompson_duck)):
                dx, dy = points_thompson_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 20 == 0:
                    sleep_for(5, 900)
                    sleep_for(30, 900)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(5, 900)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down_duck():
                    break

        elif is_mouse_down():

            for i in range(0, len(points_thompson)):
                dx, dy = points_thompson[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 20 == 0:
                    sleep_for(5, 980)
                    sleep_for(30, 980)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(5, 980)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down():
                    break


        if not thompson_spray_enabled:
            break



def cheat_mp5():
    while True:
        if is_mouse_down_duck():
            sleep_for(5, 1225)
            sleep_for(3, 1225)
            for i in range(0, len(points_mp5_duck)):
                dx, dy = points_mp5_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(1, 1225)
                    sleep_for(3, 1225)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1225)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down_duck():
                    break

        elif is_mouse_down():
            sleep_for(3, 1290)
            for i in range(0, len(points_mp5)):
                dx, dy = points_mp5[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(1, 1290)
                    sleep_for(3, 1290)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1290)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down():
                    break


        if not mp5_spray_enabled:
            break





def cheat_lr300():
    while True:
        if is_mouse_down_duck():
            sleep_for(3, 1000)
            for i in range(0, len(points_lr300_duck)):
                dx, dy = points_lr300_duck[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(21, 1000)
                    sleep_for(3, 1000)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, 1000)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down_duck():
                    break

        elif is_mouse_down():
            b=1100
            sleep_for(3, b)
            sleep_for(3, b)
            for i in range(0, len(points_lr300)):
                dx, dy = points_lr300[i]
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)
                if (i+1) % 33 == 0:
                    sleep_for(21, b)
                    sleep_for(3, b)
                    #TODO: VERIFICARE LA CARE PUNCTE FACE PAUZA 34
                else:
                    sleep_for(3, b)
                #TODO: EXISTA UN REPEAT LA POINTS PE CARE NU L AM INTRODUS
                if not is_mouse_down():
                    break


        if not lr300_spray_enabled:
            break

