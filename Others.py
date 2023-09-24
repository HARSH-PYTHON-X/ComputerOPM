from time import sleep
from tkinter import *
import pyttsx3
import speech_recognition as sr
import random
import struct

#* Speak

def speak (txt) :
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

#* LST and STR

def LST_to_STR (lst) :
    str1 = ""
 
    for ele in lst:
        str1 += ele
 
    return str1


def STR_to_LST (str) :
    li = list(str.split(" "))
    return li

#* Voice Input

def listen_command (listening_prompt = "listening ...",  command_prompt = "command >", except_prompt = "please command again ...") :
    r = sr.Recognizer()

    with sr.Microphone() as source :
        print(f"{listening_prompt}")
        audio = r.listen(source)

        try :
            cmd = r.recognize_google(audio)
            print(f"{command_prompt}", cmd)

        except Exception as e :
            print(f"{except_prompt}")
            return 'None'
        return cmd
    
def voice_input (ls_prompt = "listening ...", command_prompt = "command >", except_prmpt = "please speak again") :
    cmd = listen_command(ls_prompt, command_prompt, except_prmpt).lower().lower()
    return cmd

#* Encrypter and Decrypter

def encrypt_str (text) :
    to = list(text)

    encrypted_bin_code = []

    for char in to :
        encrypted_bin_code.append(ord(char))

    return encrypted_bin_code

def decrypt_str (bin_value) :
    message = []

    for values in bin_value :
        message.append(chr(values))

    return LST_to_STR(message)

def encrypt_num(num):
    return bin(struct.unpack('!I', struct.pack('!f', num))[0])[2:].zfill(32)

def decrypt_num(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]