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



def social_media(command):
    if 'facebook' in command:
        speak("Facebook açılıyor")
        webbrowser.open("https://www.facebook.com/")
    elif 'whatsapp' in command:
        speak("Whatsapp açılıyor")
        webbrowser.open("https://web.whatsapp.com/")
    elif 'discord' in command:
        speak("Discord açılıyor")
        webbrowser.open("https://discord.com/")
    elif 'instagram' in command:
        speak("İnstagram açılıyor")
        webbrowser.open("https://www.instagram.com/")

    elif "Linkedin" in command:
        speak("Linkedin açılıyor")
        
        
    else:
        speak("Geçerli işlem bulamadım")