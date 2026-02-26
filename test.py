import tkinter as tk
from tkinter import scrolledtext
import threading
import json
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pyttsx3

# Konuï¿½ma motoru baï¿½latma
def initialize_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Tï¿½rkï¿½e ses seï¿½imi
    turkish_voice = None
    for voice in voices:
        if "turkish" in voice.name.lower() or "tr" in voice.id.lower():
            turkish_voice = voice.id
            break
    if turkish_voice:
        engine.setProperty('voice', turkish_voice)
    else:
        engine.setProperty('voice', voices[0].id)  # Varsayï¿½lan ses
    
    # Ses hï¿½zï¿½nï¿½ (rate) ve ses tonunu (pitch) ayarlamak
    engine.setProperty('rate', 175)  # Ses hï¿½zï¿½nï¿½ biraz daha yï¿½ksek yapabilirsiniz (100-200 arasï¿½nda)
    engine.setProperty('volume', 1.0)  # Ses yï¿½ksekliï¿½i
    return engine

engine = initialize_engine()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Modeli ve verileri yï¿½kle
data = json.load(open("intents.json", encoding="utf-8"))
model = load_model("chat_model.h5", compile=False)
tokenizer = pickle.load(open("tokenizer.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

# Komut ï¿½alï¿½ï¿½tï¿½rma fonksiyonu
def execute_command(input_text):
    chat_display.insert(tk.END, f"You: {input_text}\n")

    # Model tahmini
    padded_sequences = pad_sequences(tokenizer.texts_to_sequences([input_text]), maxlen=20, truncating='post')
    result = model.predict(padded_sequences)
    tag = label_encoder.inverse_transform([np.argmax(result)])

    # Cevap seï¿½me
    for intent in data['intents']:
        if intent['tag'] == tag[0]:
            response = np.random.choice(intent['responses'])
            chat_display.insert(tk.END, f"Sancak: {response}\n")
            speak(response)  # Cevabï¿½ sesli olarak sï¿½yle
            break

# Kullanï¿½cï¿½ mesajï¿½nï¿½ alma
def send_text_command():
    user_input = text_entry.get()
    text_entry.delete(0, tk.END)
    threading.Thread(target=execute_command, args=(user_input,)).start()

# Arayï¿½z kurulumu
root = tk.Tk()
root.title("Akriha Sancak Chatbot")
root.geometry("500x600")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_display.pack(pady=10)

text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

send_button = tk.Button(root, text="Send", command=send_text_command, width=15, height=2)
send_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit, width=15, height=2)
exit_button.pack(pady=5)

# Baï¿½langï¿½ï¿½ mesajï¿½
chat_display.insert(tk.END, "Sancak: Merhaba, ben Sancak! Size nasï¿½l yardï¿½mcï¿½ olabilirim?\n")
speak("Merhaba, ben Sancak! Size nasï¿½l yardï¿½mcï¿½ olabilirim?")

root.mainloop()