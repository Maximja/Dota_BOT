import time
from actions import click_or_press
import win32gui

mid_fight_active = False

def end_game(windows):
    for hwnd in windows:  # исправлено: переменная должна быть hwnd, а не nwnd

        x_shop, y_shop = 539, 489  # Магазин (ЛКМ)
        x_butterfly, y_butterfly = 574, 358  # Бабочка (ПКМ)

        print(f"Ну все, пизда!")
        print(f"Окно {hwnd}: Открытие магазина и покупка травелов...")

        click_or_press(hwnd, x_shop, y_shop)  # Открываем магазин (ЛКМ)
        click_or_press(hwnd, x_butterfly, y_butterfly, right_click=True)  # Покупаем травела (ПКМ)
        click_or_press(hwnd, x_butterfly, y_butterfly, right_click=True)
        click_or_press(hwnd, x_shop, y_shop)  # Закрываем магазин (ЛКМ)
        time.sleep(2)
        x_end, y_end = 90, 423
        click_or_press(hwnd, x_end, y_end, press_key='a')
        time.sleep(2)






if __name__ == "__main__":
    windows = []
    win32gui.EnumWindows(
        lambda hwnd, windows: windows.append(hwnd) if "Dota 2" in win32gui.GetWindowText(hwnd) else None, windows
    )
    if not windows:
        print("❌ Окна Dota 2 не найдены.")
    else:
        end_game(windows)