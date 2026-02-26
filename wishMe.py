import datetime
import time
from initilize_engine import speak
from utils import cal_day  # Yeni modülden import ettik

# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     t = time.strftime("%H:%M")
#     day = cal_day()

#     if (hour >= 0) and (hour <= 12) and ('AM' in t):
#         speak(f"Günaydın Muhammed Ali, Nasılsın. Bugün {day} ve saat {t}")
#     elif (hour >= 12) and (hour <= 16) and ('PM' in t):
#         speak(f"Tünaydın Muhammed Ali, Bugün {day} ve saat {t}")
#     else:
#         speak(f"iyi akşamlar Muhammed Ali, Bugün {day} ve saat {t}")

def convert_time_to_text(t_str):
    saat, dakika = map(int, t_str.split(":"))

    sayilar = {
        0: "sıfır", 1: "bir", 2: "iki", 3: "üç", 4: "dört",
        5: "beş", 6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz",
        10: "on", 11: "on bir", 12: "on iki", 13: "on üç",
        14: "on dört", 15: "on beş", 16: "on altı", 17: "on yedi",
        18: "on sekiz", 19: "on dokuz", 20: "yirmi", 21: "yirmi bir",
        22: "yirmi iki", 23: "yirmi üç", 24: "yirmi dört",
        25: "yirmi beş", 26: "yirmi altı", 27: "yirmi yedi",
        28: "yirmi sekiz", 29: "yirmi dokuz", 30: "otuz",
        31: "otuz bir", 32: "otuz iki", 33: "otuz üç",
        34: "otuz dört", 35: "otuz beş", 36: "otuz altı",
        37: "otuz yedi", 38: "otuz sekiz", 39: "otuz dokuz",
        40: "kırk", 41: "kırk bir", 42: "kırk iki",
        43: "kırk üç", 44: "kırk dört", 45: "kırk beş",
        46: "kırk altı", 47: "kırk yedi", 48: "kırk sekiz",
        49: "kırk dokuz", 50: "elli", 51: "elli bir",
        52: "elli iki", 53: "elli üç", 54: "elli dört",
        55: "elli beş", 56: "elli altı", 57: "elli yedi",
        58: "elli sekiz", 59: "elli dokuz"
    }

    return f"{sayilar[saat]} {sayilar[dakika]}"

def wishMe():
    now = datetime.datetime.now()
    hour = now.hour
    t = now.strftime("%H:%M")  # 24 saat formatı
    t_text = convert_time_to_text(t)  # Türkçe saat okunuşu
    day = cal_day()

    if 0 <= hour < 12:
        speak(f"Günaydın Muhammed Ali, nasılsın. Bugün {day} ve saat {t_text}")
    elif 12 <= hour < 17:
        speak(f"Tünaydın Muhammed Ali. Bugün {day} ve saat {t_text}")
    else:
        speak(f"İyi akşamlar Muhammed Ali. Bugün {day} ve saat {t_text}")