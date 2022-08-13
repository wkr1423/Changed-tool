import win32api, win32con, win32gui
import time
input("打开changed")
window = win32gui.FindWindow(0, "Changed")
win32gui.SetForegroundWindow(window)
def pressKey(keycode):
    win32api.keybd_event(keycode, win32api.MapVirtualKey(keycode, 0), 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(keycode, win32api.MapVirtualKey(keycode, 0), win32con.KEYEVENTF_KEYUP, 0)
def up():
    pressKey(38)
    time.sleep(0.2)
    
def down():
    pressKey(40)
    time.sleep(0.2)
    
def left():
    pressKey(37)
    time.sleep(0.2)
    
def right():
    pressKey(39)
    time.sleep(0.2)
def use():
    time.sleep(0.2)
    pressKey(32)
    time.sleep(0.2)
def speedOn():
    keycode = 16
    win32api.keybd_event(keycode, win32api.MapVirtualKey(keycode, 0), 0, 0)
def speedOn():
    keycode = 16
    win32api.keybd_event(keycode, win32api.MapVirtualKey(keycode, 0), win32con.KEYEVENTF_KEYUP, 0)
def enter():
    pressKey(13)
def reload():
    pressKey(123)
def guojuqing(times):
    for t in times:
        enter()
        time.sleep(t)
    enter()

down()
down()
right()
right()
right()
up()
right()
up()
right()
right()
down()
right()
right()
up()
right()
right()
down()
right()
right()
up()
right()
right()
down()
right()
right()
right()
up()
right()
right()
down()
down()
left()
down()
left()
left()
left()
down()
left()
left()
up()
left()
left()
down()
left()
left()
up()
left()
left()
down()
left()
left()
left()
down()
right()
down()
for i in range(11):
    right()
up()
for i in range(4):
    right()