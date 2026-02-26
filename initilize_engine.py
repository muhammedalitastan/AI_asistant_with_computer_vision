
# import datetime
# import os
# import sys
# import time
# import webbrowser
# import pyautogui
# import pyttsx3 #!pip install pyttsx3
# import speech_recognition as sr
# import json
# import pickle
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import random
# import numpy as np
# import psutil 
# import subprocess

# with open("intents.json") as file:
#     data = json.load(file)

# model = load_model("chat_model.h5")

# with open("tokenizer.pkl", "rb") as f:
#     tokenizer=pickle.load(f)

# with open("label_encoder.pkl", "rb") as encoder_file:
#     label_encoder=pickle.load(encoder_file)


# def initialize_engine():
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
    
#     # Check if there is more than one voice
#     if len(voices) > 1:
#         engine.setProperty('voice', voices[0].id)  # Select the first voice
#     else:
#         engine.setProperty('voice', voices[0].id)  # Default to the first voice
    
#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', rate-60)
#     volume = engine.getProperty('volume')
#     engine.setProperty('volume', min(volume + 0.25, 1.0))  # Ensure volume doesn't exceed 1.0
    
#     return engine

# def speak(text):
#     engine = initialize_engine()
#     engine.say(text)
#     engine.runAndWait()

# def command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source, duration=0.5)
#         print("Listening.......", end="", flush=True)
#         r.pause_threshold = 1.0
#         r.phrase_threshold = 0.3
#         r.sample_rate = 48000
#         r.dynamic_energy_threshold = True
#         r.operation_timeout = 5
#         r.non_speaking_duration = 0.5
#         r.dynamic_energy_adjustment = 2
#         r.energy_threshold = 4000
#         r.phrase_time_limit = 10
#         audio = r.listen(source)
    
#     try:
#         print("\rRecognizing......", end="", flush=True)
#         query = r.recognize_google(audio, language='tr-TR')
#         print(f"\rUser said : {query}\n")
#     except Exception:
#         print("Say that again please")
#         return "None"
#     return query

import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3  #!pip install pyttsx3 # Bu satır artık sadece bilgi amaçlı, kullanılmıyor.
import speech_recognition as sr
import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np
import psutil
import subprocess
import uuid
import tempfile
# Coqui-AI TTS ve ses işleme kütüphaneleri
from TTS.api import TTS
import librosa
import soundfile as sf
from playsound import playsound
import threading # Sesin arka planda çalması için
from pydub import AudioSegment, effects
import simpleaudio as sa


# Global TTS model değişkeni
tts_model = None

# BURADAN BAŞLAYARAK YENİ KODU EKLEYECEKSİNİZ
import tensorflow as tf
import keras # Keras'ın bağımsız versiyonu da yüklü mü kontrol etmek için

print(f"TensorFlow Version: {tf.__version__}")
print(f"Keras Version (from tensorflow.keras): {tf.keras.__version__}")
print(f"Keras Version (independent Keras): {keras.__version__}") # Eğer yüklüyse
# BURAYA KADAR YENİ KOD EKLENDİ

with open("intents.json", encoding="utf-8") as file:
    data = json.load(file)

model = load_model("chat_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)


# def initialize_engine():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
    
#     # Türkçe konuşma sesi olup olmadığını kontrol et
#     turkish_voice = None
#     for voice in voices:
#         if "turkish" in voice.name.lower() or "tr" in voice.id.lower():
#             turkish_voice = voice.id
#             break
    
#     # Eğer Türkçe ses varsa, onu kullan
#     if turkish_voice:
#         engine.setProperty('voice', turkish_voice)
#     else:
#         engine.setProperty('voice', voices[0].id)  # Varsayılan ses kullan
    
#     engine.setProperty('rate', 150)  # Konuşma hızını ayarla
#     engine.setProperty('volume', 1.0)  # Ses seviyesini maksimum yap

#     return engine

class TTSEngineWrapper:
   
    SOX_PATH = r"C:\indirilen_yazılımlar\sox-14.4.2\sox.exe"  # Sınıf değişkeni

    def __init__(self):
        self.tts = TTS(model_name="tts_models/tr/common-voice/glow-tts")

    def change_pitch_with_sox(self, input_path, output_path, semitones=1):
        command = [self.SOX_PATH, input_path, output_path, "pitch", f"{semitones * 100}"]
        subprocess.run(command, check=True)

    def say(self, text):
        # Geçici dosya oluştur
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
            temp_path = tmpfile.name

        # TTS'yi dosyaya yaz
        self.tts.tts_to_file(text=text.lower(), file_path=temp_path)

        # Pitch değiştirmek için yeni dosya yolu
        pitched_path = temp_path.replace(".wav", "_pitched.wav")

        # SoX ile pitch düşür (kalınlaştır)
        self.change_pitch_with_sox(temp_path, pitched_path, semitones=0)

        # Pitched dosyayı yükle, ses artır ve hızlandır
        audio = AudioSegment.from_wav(pitched_path)
        audio = audio + 2 # +6dB ses artır
        audio = effects.speedup(audio, playback_speed=1.2)

        # Oynat
        play = sa.play_buffer(audio.raw_data, audio.channels, audio.sample_width, audio.frame_rate)
        play.wait_done()

        # Geçici dosyaları sil
        os.remove(temp_path)
        os.remove(pitched_path)

    def runAndWait(self):
        # Şimdilik boş, say() zaten senkron oynatıyor
        pass

def initialize_engine():
    return TTSEngineWrapper()          


def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Dinliyorum.......", end="", flush=True)
        r.pause_threshold = 1.0
        r.phrase_threshold = 0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold = True
        r.operation_timeout = 5
        r.non_speaking_duration = 0.5
        r.dynamic_energy_adjustment = 2
        r.energy_threshold = 4000
        r.phrase_time_limit = 10
        audio = r.listen(source)
    
    try:
        print("\rTanımlıyorum......", end="", flush=True)
        query = r.recognize_google(audio, language='tr-TR')  # Türkçe dil modeli
        print(f"\rKullanıcı dedi ki: {query}\n")
    except Exception:
        print("Tekrar söyler misiniz?")
        return "None"
    return query
