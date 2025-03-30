import time
from actions import click_or_press


mid_fight_active = True  # Флаг активности пиздилова в миду

def mid_fight(windows):
    """Цикл пиздилова в миду"""
    x_mid, y_mid = 54, 454  # Координаты для пиздилова в миду

    while True:
        if mid_fight_active:
            for hwnd in windows:
                click_or_press(hwnd, x_mid, y_mid, press_key='a')  # Нажимаем "A" для пиздилова
                time.sleep(1)
        time.sleep(10)

if __name__ == "__main__":
    # Код для поиска окон
    import win32gui

    windows = []
    win32gui.EnumWindows(
        lambda hwnd, windows: windows.append(hwnd) if "Dota 2" in win32gui.GetWindowText(hwnd) else None, windows
    )

    if not windows:
        print("❌ Окна Dota 2 не найдены.")
    else:
        mid_fight(windows)
