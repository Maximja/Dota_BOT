import threading
import win32gui
from mid_fight import mid_fight
from buy_items import buy_items

def main():
    windows = []
    win32gui.EnumWindows(
        lambda hwnd, windows: windows.append(hwnd) if "Dota 2" in win32gui.GetWindowText(hwnd) else None, windows
    )

    if not windows:
        print("❌ Окна Dota 2 не найдены.")
        return

    # Запускаем пиздилово в миду в отдельном потоке
    fight_thread = threading.Thread(target=mid_fight, args=(windows,), daemon=True)
    fight_thread.start()

    # Запускаем покупку предметов в отдельном потоке
    buy_thread = threading.Thread(target=buy_items, args=(windows,))
    buy_thread.start()

if __name__ == "__main__":
    main()
