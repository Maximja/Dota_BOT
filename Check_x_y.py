import win32gui
from pynput import mouse

# Получаем координаты окна Dota 2
def get_dota_window():
    hwnd = win32gui.FindWindow(None, "Dota 2")
    if hwnd:
        rect = win32gui.GetWindowRect(hwnd)
        return hwnd, rect  # Возвращаем дескриптор окна и его координаты
    return None, None

# Обработчик кликов
def on_click(x, y, button, pressed):
    if pressed:  # Фиксируем только нажатие
        hwnd, rect = get_dota_window()
        if hwnd:
            window_x, window_y = rect[0], rect[1]  # Верхний левый угол окна
            relative_x = x - window_x  # Смещаем координаты относительно окна
            relative_y = y - window_y
            print(f"🎯 Координаты клика внутри окна Dota 2: ({relative_x}, {relative_y})")
        else:
            print("❌ Окно Dota 2 не найдено!")

# Запускаем слушатель кликов
with mouse.Listener(on_click=on_click) as listener:
    print("🚀 Кликни в окне Dota 2, чтобы узнать координаты относительно него.")
    print("❌ Закрой программу, чтобы выйти.")
    listener.join()
