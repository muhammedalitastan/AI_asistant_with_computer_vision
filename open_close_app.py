
import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3 #!pip install pyttsx3
import speech_recognition as sr
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np
import psutil 
import subprocess
from initilize_engine import initialize_engine, command,speak
from utils import cal_day  # Artık burada doğrudan çağırabiliyoruz
from wishMe import wishMe
from social_media import social_media

def openApp(command):
    if "calculator" in command:
        speak("opening calculator")
        subprocess.Popen(["calc.exe"], shell=True)  # Windows 10/11 için
    elif "notepad" in command:
        speak("opening notepad")
        os.startfile('C:\\Windows\\System32\\notepad.exe')
    elif "paint" in command:
        speak("opening paint")
        os.startfile('C:\\Windows\\System32\\mspaint.exe')
    elif "yazılım programı" in command:
        speak("opening visiual studio")
        os.startfile("Visual Studio Code.lnk")
    elif "eclipse" in command:
        speak("opening eclipse")
        os.startfile("Eclipse IDE for Enterprise Java and Web Developers - 2024-06.lnk")    

    



def closeApp(command):
    if "calculator" in command:
        speak("closing calculator")
        for proc in psutil.process_iter(attrs=['pid', 'name']):
            if proc.info['name'].lower() in ["calc.exe", "calculatorapp.exe"]:
                os.kill(proc.info['pid'], 9)  # Süreci sonlandır
                print("Calculator closed.")
                return
    
    elif "notepad" in command:
        speak("closing notepad")
        os.system('taskkill /f /im notepad.exe')
    elif "paint" in command:
        speak("closing paint")
        os.system('taskkill /f /im mspaint.exe')


