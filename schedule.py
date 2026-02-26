import tkinter as tk
import json

# Dosyadan veriyi oku
def load_schedule():
    try:
        with open("schedule.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Eğer dosya yoksa boş bir sözlük döndür

# Veriyi dosyaya yaz
def save_schedule():
    with open("schedule.json", "w") as file:
        json.dump(week, file, indent=4)

def update_schedule():
    day = day_entry.get().lower()
    task = task_entry.get()
    if day and task:
        week[day] = task
        schedule_text.set(f"Updated {day.capitalize()}\n\n{task}")
        print(f"Updated {day.capitalize()}: {task}")  # Print the updated schedule
        save_schedule()  # Veriyi kaydet
        return day, task  # Return the updated day and task
    else:
        schedule_text.set("Please enter both day and task!")
        return None, None  # If nothing is entered, return None

def get_schedule():
    day = day_entry.get().lower()
    schedule = week.get(day, "No schedule available")
    schedule_text.set(schedule)
    print(f"Schedule for {day.capitalize()}: {schedule}")  # Print the schedule for the selected day
    return schedule  # Return the current schedule for the selected day

# Initial Schedule Dictionary, verileri dosyadan oku
week = load_schedule()

# GUI Setup
root = tk.Tk()
root.title("Daily Schedule Manager")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

schedule_text = tk.StringVar()

title_label = tk.Label(root, text="Schedule Manager", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

day_label = tk.Label(root, text="Enter Day:", font=("Arial", 12), bg="#f0f0f0")
day_label.pack()

day_entry = tk.Entry(root, font=("Arial", 12))
day_entry.pack(pady=5)

task_label = tk.Label(root, text="Enter Task:", font=("Arial", 12), bg="#f0f0f0")
task_label.pack()

task_entry = tk.Entry(root, font=("Arial", 12), width=40)
task_entry.pack(pady=5)

update_button = tk.Button(root, text="Update Schedule", font=("Arial", 12, "bold"), command=update_schedule, bg="#4CAF50", fg="white", padx=10, pady=5)
update_button.pack(pady=10)

fetch_button = tk.Button(root, text="Get Schedule", font=("Arial", 12, "bold"), command=get_schedule, bg="#008CBA", fg="white", padx=10, pady=5)
fetch_button.pack(pady=5)

schedule_label = tk.Label(root, textvariable=schedule_text, font=("Arial", 12), bg="#ffffff", wraplength=350, justify="left", padx=10, pady=10, relief="solid")
schedule_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit, bg="#FF5733", fg="white", padx=10, pady=5)
exit_button.pack(pady=5)

root.mainloop()
