from time import sleep
from tkinter import *
import random

#* Constant Values

const_G = 0.00000000006

const_g_equator = 9.8
const_g_pole = 10

#* Main

def momentum_of (mass, velocity) :
    momentum = mass * velocity
    return momentum

def kinetic_energy_of_obj_from_height (mass, height) :
    kinetci_energy = mass * height
    return kinetci_energy

def kinetic_energy_of_obj (mass, velocity) :
    kinetic_energy = 1 / 2 * mass * velocity * velocity
    return kinetic_energy

def find_height_from_time (time_taken_from_down_to_up_and_up_to_down) :
    height = time_taken_from_down_to_up_and_up_to_down * time_taken_from_down_to_up_and_up_to_down * 4.9
    return height