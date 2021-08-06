import time
import pyautogui
from PIL import ImageGrab


def has_collided(loaded_img):
    # for n in range(770, 830):
    #     for m in range(390, 410):
    #         if loaded_img[n, m] < 100:
    #             press('down')
    #             return
    print('before the for loop')
    for n in range(770, 790):
        for m in range(390, 420):
            print('before if')
            if loaded_img[n, m] < 100:
                print('in if')
                pyautogui.press("up")
                print('pressed up')

                return

    return


if __name__ == '__main__':
    screen_width, screen_height = pyautogui.size()

    current_mouseX, current_mouseY = pyautogui.position()

    pyautogui.moveTo(233, 1043)
    pyautogui.leftClick()
    time.sleep(3)

    pyautogui.hotkey('command', 't')
    time.sleep(0.5)

    pyautogui.leftClick(209, 83)
    pyautogui.write('https://elgoog.im/t-rex/', interval=0.1)
    pyautogui.press('enter')

    time.sleep(1.5)

    pyautogui.press('up')

    game_on = True

    while game_on:
        dino_img = ImageGrab.grab().convert('L')
        loaded_dino_img = dino_img.load()
        has_collided(loaded_dino_img)

        #
        # for n in range(770, 830):
        #     for m in range(390, 410):
        #         if loaded_dino_img[n, m] < 100:
        #             press('down')
        #
        # for n in range(745, 765):
        #     for m in range(390, 420):
        #         loaded_dino_img[n, m] = 0
        #
        # time.sleep(1.5)
        # dino_img.show()