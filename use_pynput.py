from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def press_and_release(key):
    keyboard.press(key)
    time.sleep(0.1)
    keyboard.release(key)


if __name__ == "__main__":
    while True:
        press_and_release("c")
        time.sleep(1)