import win32gui
import win32con
import time
import pyautogui

def activate_window(hwnd):
    """Активирует окно, используя клик, если `SetForegroundWindow` не срабатывает, и нажимает Enter"""
    try:
        # Разворачиваем окно, если оно свернуто
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.4)  # Даем время на восстановление

        # Перемещаем курсор в центр окна и кликаем
        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0] + 100, rect[1] + 100  # Кликаем ближе к левому верхнему углу


        pyautogui.click()  # Кликаем в окно, чтобы активировать
        time.sleep(0.2)  # Ждем

        # Пробуем сделать окно активным
        win32gui.BringWindowToTop(hwnd)
        win32gui.SetForegroundWindow(hwnd)

        print(f"✅ Окно {hwnd} активировано!")

        # Нажимаем ENTER

        pyautogui.press('enter')
        print(f"✅ ENTER нажат в окне {hwnd}!")

    except Exception as e:
        print(f"❌ Ошибка активации окна {hwnd}: {e}")

def preload_windows(windows):
    """Переключаемся на каждое окно с небольшой задержкой и нажимаем Enter"""
    print("⏳ Начинаем ускоренную загрузку окон...")

    for hwnd in windows:
        print(f"🔄 Открываем окно {hwnd}...")
        activate_window(hwnd)
        time.sleep(0.2)  # Даем время на обработку

    print("✅ Все окна активированы!")

def main():
    # Получаем все окна с названием "Dota 2"
    windows = []
    win32gui.EnumWindows(
        lambda hwnd, windows: windows.append(hwnd) if "Dota 2" in win32gui.GetWindowText(hwnd) else None, windows
    )

    if not windows:
        print("❌ Окна Dota 2 не найдены.")
        return

    preload_windows(windows)  # Поочередно активируем окна и нажимаем Enter

if __name__ == "__main__":
    main()
