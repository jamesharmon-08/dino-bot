from PIL import Image
from mss import mss
from pynput.keyboard import Key, Controller
import time

monitor = {"top": 430, "left": 460, "width": 16, "height": 32,}

keyboard = Controller()
running = True
ctr=0


ctr = 0
while running:
    ctr +=1

    with mss() as sct:
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", (sct_img.size), sct_img.rgb).convert("L")
    pixels = list(img.getdata())

    for pixel in pixels:
        if pixel < 100:
            keyboard.press(Key.up)
            time.sleep(.250)
            keyboard.release(Key.up)
            break
    if ctr>10000:
        running = False

