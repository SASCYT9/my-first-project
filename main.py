import pyautogui
from PIL import ImageGrab
import keyboard
import random
print("Наведіть мишку на потрібне місце і натисніть SPACE")

selected_pos = None
target_color = None

def on_space():
    global selected_pos, target_color
    selected_pos = pyautogui.position()
    screenshot = ImageGrab.grab()
    target_color = screenshot.getpixel(selected_pos)
    print(f"Збережено: позиція {selected_pos}, колір {target_color}")

keyboard.on_press_key("space", lambda _: on_space())
keyboard.wait("esc")
# Це коментар для гітхабу : Збереження позиції та кольору завершено. Натисніть ESC для виходу.