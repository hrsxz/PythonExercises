# -*- coding: utf-8 -*-
"""
Created on Sun May  9 13:16:07 2021

@author: xisong
"""

import pyautogui
import time
import sys
import os

# sys.path.append('C:\ProgramData\Anaconda3\Lib\site-packages\pyautogui')
# Global settings
pyautogui.pause = 1
pyautogui.failsafe = True

# Get resulution
width, height = pyautogui.size()
print('Monitor resulution: ' + str(width) + ' * ' + str(height))


try:
    while True:
        # Get mouse position
        x, y = pyautogui.position()
        MousePosition = 'Mouse actual position: (' + str(x) + ', '+str(y) + ')'
        print(MousePosition, end='')
        print('\b' * len(MousePosition) , sep='', end='',flush=True)
#        print('{}\r'.format(MousePosition), end='')
        if (x + 1 < width - 1) and (y + 1 < height - 1):
            pyautogui.moveTo(x+1,y+1,0.01)
        elif  x - 1 > 0 and y -1 > 0:
            pyautogui.moveTo(x-1,y-1,0.01)
        else:
            pyautogui.moveTo(x+1,y+1,0.01)
#        os.system('cls')
        time.sleep(1)

except KeyboardInterrupt:
    print('\nKeyboard interrupt, process stopped.')
    sys.exit()