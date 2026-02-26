import datetime

def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {
        1: "Pazartesi",
        2: "Salı",
        3: "Çarşamba",
        4: "Perşembe",
        5: "Cuma",
        6: "Cumartesi",
        7: "Pazar"
    }
    return day_dict.get(day, "Unknown")
