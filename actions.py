import win32gui
import pyautogui
import time

def click_or_press(hwnd, x_offset, y_offset, right_click=False, press_key=None):
    """Функция для клика (ЛКМ, ПКМ) или нажатия клавиши внутри окна"""
    try:
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(0.5)  # Даем время для фокуса

        rect = win32gui.GetWindowRect(hwnd)
        x, y = rect[0] + x_offset, rect[1] + y_offset

        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(0.5)  # Даем время перед действием

        if press_key:
            pyautogui.press(press_key)
            print(f"✅ Нажата клавиша '{press_key}' в окне {hwnd}")
        elif right_click:
            pyautogui.rightClick()
            print(f"✅ ПКМ в окне {hwnd} по координатам ({x}, {y})")
        else:
            pyautogui.click()
            print(f"✅ ЛКМ в окне {hwnd} по координатам ({x}, {y})")

    except Exception as e:
        print(f"❌ Ошибка в окне {hwnd}: {e}")
