from time import sleep
import random
from Math import *
from Others import *
import os
from tkinter import *
import keyboard
from math import *

def initiate_XOS () :

    #* MAIN MENU

    print("welcome to __XOS__ ...")
    print("use [ ls ] to list menu ...")

    print()

    Menu = [
        "random [ran]",
        "calculator [cal]",
        "scripter [sc]",
        "catch game [cg]", 
        "txt_to_speech [tsp]",
        "height_finder [hf]",
        "code editor x [ CEX ]"
    ]

    #! FUNCTIONS

    info = [
        "__XOS__ stands for [ X operating system ]",
        "This system is built for time pass during computer classes" ,
        "The OS contains many games, some are 2 - 3 players",
        "This OS is developed by -> Harsh Pro",
        "Ha bhai mene he banaya hai ..."
    ]

    def show_menu (menu) :
        print()
        for ele in menu :
            print(ele)
        print()

    def CEX () :
        print()
        print("welcome to CEX [ code editor X ]")
        print("type - [ run ] to run programme ...")
        print()

        command = []

        while True :
            cmd = input(">>")

            command.append(cmd)

            if cmd == "run" :
                command.remove('run')
                for execute in command :
                    exec(execute)

            elif cmd == "quit" :
                break

            elif cmd == "exit" :
                break

        print("exited - code editor X [ CEX ]")

        print()

    def calculator () :
        print()

        work = int(input("basic calculations [0], AP [1] >"))

        if work == 0 :
            n1 = float(input("num1 >"))
            func = input("fucntion >")

            if func == "+" :
                n2 = float(input("num2 >"))
                print(n1 + n2)

            elif func == "-" :
                n2 = float(input("num2 >"))
                print(n1 - n2)

            elif func == "*" :
                n2 = float(input("num2 >"))
                print(n1 * n2)

            elif func == "/" :
                n2 = float(input("num2 >"))
                print(n1 / n2)

            elif func == "**" :
                print(n1 * n1)

            elif func == "//" :
                print(n1 ** 0.5)

            else :
                print("invalid ! ...")

        elif work == 1 :
            pass

        else :
            print("invalid ! ...")

        print()

    def random () :
        print()
        work = int(input("random - int [0], list[1] >"))

        if work == 0 :
            start = int(input("start >"))
            end = int(input("end >"))

            print(random_int(start, end))

        elif work == 1 :
            group = input("list >")
            length = int(input("length >"))

            print(choose_random(STR_to_LST(group), length))

        else :
            print("wrong input ! ...")

        print()


    def catch_game () :
        window = Tk()

        btn = Button(text = "quit", fg = "red", command = lambda:window.destroy())
        btn.grid(column = 0, row = 0)

        window.mainloop()

    def height_finder () :
        print()

        by_type = int(input("type - Trignometery [0], Physics [1] >"))

        if by_type == 0 :
            distance = float(input("distance >"))
            angle = int(input("angle >"))

            angles = [
                [30, 1 / sqrt(3)],
                [45, 1],
                [60, sqrt(3)]
            ]

            for found_angle in angles :
                if angle in found_angle :
                    print(found_angle[1] * distance)

        elif by_type == 1 :
            time_we_need = float(input("total time taken till peak height >"))

            print(time_we_need * time_we_need * 4.9)

        print()

    #! TASK LINE

    while True :
        cmd = input("->")
        
        if cmd == "menu" :
            show_menu(Menu)

        #! code editor X

        elif cmd == "CEX" :
            CEX()

        elif cmd == "cex" :
            CEX()

        elif cmd == "code editor X" :
            CEX()

        elif cmd == "code editor x" :
            CEX()

        #!

        elif cmd == "info" :
            show_menu(info)

        elif cmd == "ls" :
            show_menu(Menu)

        elif cmd == "cal" :
            calculator()

        elif cmd == "calculator" :
            calculator()

        elif cmd == "speak" :
            print()
            txt = input("txt >")
            speak(txt)
            print()

        elif cmd == "tsp" :
            print()
            txt = input("txt >")
            speak(txt)
            print()

        elif cmd == "cg" :
            catch_game()

        elif cmd == "random" :
            random()

        elif cmd == "ran" :
            random()

        elif cmd == "hf" :
            height_finder()

        elif cmd == "height_finder" :
            height_finder()

        #* CLEAR code

        #! EXIT CODES

        elif cmd == "q" :
            print()
            print("successfully exited ...")
            break

        elif cmd == "exit" :
            print()
            print("successfully exited ...")
            break

        elif cmd == "quit" :
            print()
            print("successfully exited ...")
            break

        else :
            continue