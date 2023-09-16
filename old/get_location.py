import pyautogui, time








while True:
    time.sleep(1)
    currentMouseX, currentMouseY = pyautogui.position() 
    print (currentMouseX, currentMouseY)