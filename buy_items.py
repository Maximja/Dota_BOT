import time


from actions import click_or_press

mid_fight_active = False  # Флаг активности пиздилова в миду1

def buy_items(windows):
    x_shop, y_shop = 539, 489  # Магазин (ЛКМ)
    x_travel, y_travel = 529, 362  # Травела (ПКМ)
    x_desol, y_desol = 549, 360  # Дезоль (ПКМ)

    # x_butterfly, y_butterfly = 574, 358  # Бабочка (ПКМ)


    # Ожидание 10 минут до начала первой покупки (например, пиздилово уже идет)
    print("⏳ Ожидание 10 минут перед покупкой травелов...")
    time.sleep(600)  # 10 минут до первой покупки

    for hwnd in windows:
        print(f"Окно {hwnd}: Открытие магазина и покупка травелов...")
        click_or_press(hwnd, x_shop, y_shop)  # Открываем магазин (ЛКМ)
        click_or_press(hwnd, x_travel, y_travel, right_click=True)  # Покупаем травела (ПКМ)
        click_or_press(hwnd, x_shop, y_shop)  # Закрываем магазин (ЛКМ)
        time.sleep(1)

    # Возобновляем пиздилово в миду после покупки травелов
    print("✅ Травела куплены, пиздилово продолжено.")

    # Ожидание 5 минут до остановки пиздилова для покупки дезоля
    print("⏳ Ожидание 5 минут до покупки дезоля...")
    time.sleep(300)  # 5 минут ожидания

    # Останавливаем пиздилово в миду для покупки дезоля
    mid_fight_active = False
    print("⏸️ Пиздилово остановлено для покупки дезоля.")

    for hwnd in windows:
        print(f"Окно {hwnd}: Открытие магазина и покупка дезоля...")
        click_or_press(hwnd, x_shop, y_shop)  # Открываем магазин (ЛКМ)
        click_or_press(hwnd, x_desol, y_desol, right_click=True)  # Покупаем дезоль (ПКМ)
        click_or_press(hwnd, x_shop, y_shop)  # Закрываем магазин (ЛКМ)
        time.sleep(1)

    # Возобновляем пиздилово после покупки дезоля
    mid_fight_active = True
    print("✅ Дезоль куплен, пиздилово возобновлено.")

    print("✅ Покупка предметов завершена.")

mid_fight_process = True
print("Пиздилово в миду началось...")

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
        buy_items(windows)
