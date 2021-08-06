# import keyboard
# def ss():
#     ss = pyautogui.screenshot()
#     print(ss.save(r'./images/ss.png'))
#     return
# while True:
#     if keyboard.is_pressed('q'):
#         break

# from curtsies import Input
#
# def main():
#     with Input(keynames='curses') as input_generator:
#         for e in input_generator:
#             print(repr(e))
#
# if __name__ == '__main__':
#     main()
import pygame
from pygame.locals import *
import sys
while True:
    print("gfgc")
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

