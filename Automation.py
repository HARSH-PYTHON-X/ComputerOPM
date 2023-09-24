from Math import *
from Physics import *
from Others import *
from Others import *
import pyautogui as pg
import pydirectinput as pd
import keyboard

#* Detect key press

def detect_KeyPress (key = None, output = None, threshold = 0.1) :
    if keyboard.is_pressed(key) :
        sleep(threshold)
        output()

#* key pressing

def PressKey (key = None) :
    pd.press(key)

def HoldKeyDown (key = None) :
    pd.keyDown(key)

def HoldKeyUp (key = None) :
    pd.keyUp(key)

def HoldKeyForTime (key = None, time = None) :
    HoldKeyDown(key)
    sleep(time)
    HoldKeyUp(key)

#* Mouse Movement

def PressMouseLeft () :
    pd.leftClick()

def PressMouseRight () :
    pd.rightClick()

def PressMouseMiddle () :
    pd.middleClick()

def MoveMouseTo (cords = (0, 0), TimeToReach = 0) :
    pd.moveTo(cords[0], cords[1], TimeToReach)

#* Game Bot

def MOUSEKEY_LEFT () :
    return "left"

def MOUSEKEY_RIGHT () :
    return "right"

class Bot :
    def jump () :
        PressKey("Space")

    def crouch_Toggle (key = "c") :
        detect_KeyPress(key)

    def Place_Block (key = MOUSEKEY_LEFT) :
        if key == "left" :
            PressMouseLeft()

        elif key == "right" :
            PressMouseRight()

    def Destroy_Block (key = MOUSEKEY_RIGHT) :
        if key == "left" :
            PressMouseLeft()

        elif key == "right" :
            PressMouseRight()

    def Jump_Block (threshold = 0.2, KeyToPlace = MOUSEKEY_LEFT) :
        PressKey("Space")
        sleep(threshold)

        if KeyToPlace == "left" :
            PressMouseLeft()

        elif KeyToPlace == "right" :
            PressMouseRight()