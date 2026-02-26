# import tkinter as tk
# from tkinter import scrolledtext
import threading
from initilize_engine import command, speak
from social_media import social_media
from open_close_app import openApp, closeApp
from condition import condition
from Browsing import browsing
from wishMe import wishMe
from utils import cal_day
import subprocess
import json
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from arayuz_gui import ChatWindow,LoginWindow,SignupWindow
from PyQt5.QtWidgets import QApplication, QStackedWidget 
import sys



# def send_text_command():
#     """Kullanıcının metin girişini alıp execute_command fonksiyonunu çalıştırır."""
#     user_input = text_entry.get()
#     text_entry.delete(0, "end")  # Giriş kutusunu temizle
#     threading.Thread(target=execute_command, args=(user_input,)).start()

# def start_listening():
#     """Sesli komutları dinleyip execute_command fonksiyonunu çalıştırır."""
#     threading.Thread(target=execute_command).start()

# root, chat_display, text_entry = arayüz(send_text_command,start_listening)


class WindowManager(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Life Twin Chatbot")
        self.setGeometry(200, 100, 480, 640) # Ana pencere boyutları
        
        self.login_window = LoginWindow(self.show_chat_window, self.show_signup_window)
        self.signup_window = SignupWindow(self.show_login_window)
        
        self.addWidget(self.login_window)
        self.addWidget(self.signup_window)
        
        # Başlangıçta giriş ekranını göster
        self.setCurrentWidget(self.login_window)

    def show_login_window(self):
        self.setCurrentWidget(self.login_window)

    def show_signup_window(self):
        self.setCurrentWidget(self.signup_window)

    def show_chat_window(self, user_email):
        # ChatWindow'u her seferinde yeniden oluşturmak yerine, bir kez oluşturup saklayabiliriz.
        # Ancak execute_command ve command fonksiyonlarını parametre olarak beklediği için
        # şimdilik her seferinde yeniden oluşturmak daha güvenli.
        self.chat_window = ChatWindow(user_email, execute_command, command)
        self.addWidget(self.chat_window)
        self.setCurrentWidget(self.chat_window)


def main():
    app = QApplication(sys.argv)
    manager = WindowManager()
    manager.show()
    sys.exit(app.exec_())


def load_schedule():
    with open("schedule.json", "r", encoding="utf-8") as file:
        return json.load(file)

def schedule1():
    schedule_data = load_schedule()
    day = cal_day().lower()
    speak("Boss, today's schedule is")
    if day in schedule_data:
        speak(schedule_data[day])
    else:
        speak("Boss, I couldn't find a schedule for today.")

process = None
process2=None

def openSchedule():
    global process
    if process is None:
        process = subprocess.Popen(["python", "schedule3.py"])


def closeSchedule():
    global process
    if process is not None:
        process.terminate()
        process = None

def openDaily():
    global process2
    if process is None:
        process2 = subprocess.Popen(["python", "günlük.py"])

def closeDaily():
    global process2
    if process is not None:
        process.terminate()
        process2 = None   

def connectwifi():
    global process
    if process is None:
        process = subprocess.Popen(["python", "wifi_bağlanma.py"])

def closewifi():
    global process2
    if process is not None:
        process.terminate()
        process2 = None 
             
def openfaceid():
    global process
    if process is None:
        process= subprocess.Popen(["python","Faceid.py"])





def execute_command(input_text=None, chat_window_instance=None):
    query = input_text if input_text else command().lower()
    # chat_display.insert(tk.END, f"You: {query}\n")
    
    if chat_window_instance: # PyQt5 arayüzüne mesajı ekle
        chat_window_instance.add_message(f"You: {query}", is_user=True)
     
    if any(word in query for word in ['facebook', 'discord', 'whatsapp', 'instagram']):
        social_media(query)
    elif "volume up" in query or "increase volume" in query:
        speak("Volume increased")
    elif "volume down" in query or "decrease volume" in query:
        speak("Volume decreased")
    elif "mute the sound" in query:
        speak("Volume muted")
    elif "open calculator" in query or "open notepad" in query or "open paint" in query or "yazılım programını aç" in query:
        openApp(query)
    elif "close calculator" in query or "close notepad" in query or "close paint" in query:
        closeApp(query)
    elif "takvimi aç" in query:
        openSchedule()
    elif "kendini tanıt" in query:
        speak("Merhaba ben Orbit. Atom teknoloji tarafından geliştirilmiş bir yapay zeka chabotum. İnsanların bir çok alışılmış işlerini yerine getirerek klavye kullanımını ve zaman kaybını önlemiş oluyorum. Tanıştığımıza memnun oldum. Denemek için bana sorular sorabilirsin")
    elif "close schedule" in query:
        closeSchedule()
    elif "tell me today work" in query:
        schedule1()

    elif "connect to wifi" in query:
        connectwifi()
    elif "disconnect from wifi" in query:
        closewifi()        
    elif any(kelime in query for kelime in ["ne", "kim", "nasıl", "merhaba", "teşekkürler", "selam"]):
        padded_sequences = pad_sequences(tokenizer.texts_to_sequences([query]), maxlen=20, truncating='post')
        result = model.predict(padded_sequences)
        tag = label_encoder.inverse_transform([np.argmax(result)])
        for i in data['intents']:
            if i['tag'] == tag:
                response = np.random.choice(i['responses'])
                if chat_window_instance: # PyQt5 arayüzüne mesajı ekle
                    chat_window_instance.add_message(f"JARVIS: {response}", is_user=False)
                speak(response)

    elif "open google" in query or "open edge" in query:
        browsing(query)
    elif "open daily" in query or "open daily note" in query:
        openDaily()
    elif "close daily" in query:
        closeDaily()        
    elif "system condition" in query:
        speak("Checking the system condition")
        condition()
    elif "yazıma başla" in query:
        speak("Muhammed Ali emin misin?, bunun için mausu yazılacak alana tıkla ve konuşmaya başla")
        if "evet başla" in query:
            speak("Yazım 10 saniye içinde ses kayıtı ile birlikte başlayacak")

    elif "exit" in query:
        QApplication.instance().quit() # PyQt5 uygulamasını kapatma komutu
    return query
       

def start_listening():
    threading.Thread(target=execute_command).start()

def send_text_command():
    user_input = text_entry.get()
    text_entry.delete(0, tk.END)
    threading.Thread(target=execute_command, args=(user_input,)).start()

# Load AI Model
data = json.load(open("intents.json", encoding="utf-8"))
model = load_model("chat_model.h5", compile=False)
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))



wishMe()
speak("Merhaba efendim , Ben Orbit size nasıl yardımcı olabilirim? ")

if __name__ == "__main__":
    main()

