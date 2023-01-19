import pyautogui
import time
import sys
import signal
import time
from datetime import datetime
pyautogui.FAILSAFE = False

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

timeoutSeconds = None
if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    timeoutSeconds = 100
else:
    timeoutSeconds = int(sys.argv[1])
print("Timeout: {} seconds".format(timeoutSeconds))

screenWidth, screenHeight = pyautogui.size()
start = time.time()
PERIOD_OF_TIME = 8*60*60 # 8 hours

while(True):
    time.sleep(timeoutSeconds)
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX > screenWidth/2:
        moveX = -1
    else:
        moveX = 1
    if currentMouseY > screenHeight/2:
        moveY = -1
    else:
        moveY = 1
    pyautogui.moveTo(currentMouseX+moveX, currentMouseY+moveY)
    for i in range(0,3):
        pyautogui.press("shift")
    print("wake up made at {}".format(datetime.now().time()))
    if time.time() > start + PERIOD_OF_TIME : break
