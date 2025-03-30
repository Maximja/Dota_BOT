import subprocess
import time
import threading
import tkinter as tk

# Переменные для процессов
mid_fight_process = None
buy_items_process = None

def start_mid_fight():
    global mid_fight_process
    print("Запуск процесса mid_fight...")
    mid_fight_process = subprocess.Popen(["python", "mid_fight.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Процесс mid_fight запущен")

def start_buy_items():
    global buy_items_process
    print("Запуск процесса buy_items...")
    buy_items_process = subprocess.Popen(["python", "buy_items.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Процесс buy_items запущен")

def stop_processes():
    if mid_fight_process:
        print("Остановка процесса mid_fight...")
        mid_fight_process.terminate()
    if buy_items_process:
        print("Остановка процесса buy_items...")
        buy_items_process.terminate()

    print("Процессы остановлены")

# GUI с использованием Tkinter
def create_gui():
    window = tk.Tk()
    window.title("Bot Control")

    start_mid_fight_button = tk.Button(window, text="Начать пиздилово", command=start_mid_fight)
    start_mid_fight_button.pack(pady=5)

    start_buy_items_button = tk.Button(window, text="Купить предметы", command=start_buy_items)
    start_buy_items_button.pack(pady=5)

    stop_button = tk.Button(window, text="Стоп", command=stop_processes)
    stop_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
