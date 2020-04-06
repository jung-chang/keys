import os
import time
import random
import pyautogui
import random
from elevate import elevate

class Box():

    def __init__(self, top, left, width, height):
        self.top = top
        self.left = left
        self.width = width
        self.height = height


class Keys():

    def __init__(self):
        self.images_path = os.path.abspath("images/laptop")
        self.keyboard_layout = [
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l"],
            ["z", "x", "c", "v", "b", "n", "m"]]
        self.q = self._get_box("q.PNG")

        # Map letter
        x, y = self._get_center(self.q)
        for i, row in enumerate(self.keyboard_layout):
            for j, key in enumerate(row):
                top = self.q.top + self.q.height * i
                left_offset = i * self.q.width // 2
                left = self.q.left + left_offset + self.q.width * j
                setattr(self, key, Box(top, left, self.q.width, self.q.height))

        # Map special keys
        self.alt = self._get_box("alt.png")
        self.up = self._get_box("up.png")
        self.down = self._get_box("down.png")
        self.left = self._get_box("left.png")
        self.right = self._get_box("right.png")

    def _get_box(self, image):
        box = pyautogui.locateOnScreen(os.path.join(self.images_path, image), confidence=0.6)
        if not box:
            print("Failed to get box for ", image)
        return Box(box.top, box.left, box.width, box.height)

    def _get_center(self, box):
        return box.left + box.width // 2, box.top + box.height // 2

    def click(self, box):
        pyautogui.click(self._get_center(box))

    def hold(self, box, pause):
        x, y = self._get_center(box)
        pyautogui.mouseDown(button='left', x=x, y=y)
        time.sleep(pause)
        pyautogui.mouseUp(button='left', x=x, y=y)


keys = Keys()

def flash_jump_attack():
    keys.click(keys.alt)
    time.sleep(random.uniform(0.05, 0.15))
    keys.click(keys.alt)
    time.sleep(0.1)
    keys.click(keys.alt)
    keys.click(keys.c)
    time.sleep(0.1)
    keys.click(keys.c)
    time.sleep(random.uniform(0.05, 0.1))
    keys.click(keys.c)
    time.sleep(random.uniform(0.05, 0.1))
    keys.click(keys.c)

def run_jump_attack(direction_key):
    keys.hold(direction_key, 1)
    keys.click(keys.alt)
    time.sleep(0.1)
    keys.click(keys.c)


def main():
    elevate()
    time.sleep(2)
    print("Start")
    change_direction = 5
    right = True
    count = 1
    while True:
        if count % change_direction == 0:
            print("Turn")
            right = not right
        run_jump_attack(keys.right if right else keys.left)
        if random.choice([True, False]):
            time.sleep(0.5)
            keys.click(keys.x)
            time.sleep(0.1)
            keys.click(keys.x)
        count += 1
        print(count)
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input()