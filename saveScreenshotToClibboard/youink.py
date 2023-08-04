import pyautogui
import pyclip
import io
import keyboard
from PIL import ImageGrab

def save_to_clipboard():
    print("click")
    screenshot = ImageGrab.grab()

    # convert to array of bytes
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format="PNG")
    img_bytes = img_bytes.getvalue()

    # save to clipboard
    pyclip.copy(img_bytes)
  

def main():
    keyboard.add_hotkey('print_screen', save_to_clipboard)

    try:
        print('Listening... Press Ctrl+c to exit')
        keyboard.wait('ctrl+c')
    except KeyboardInterrupt:
        print("OFF")
        keyboard.unhook_all()


if __name__ == "__main__":
    main()