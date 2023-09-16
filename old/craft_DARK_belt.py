import pyautogui, time







# location 
# 1670 2105
def craft_fine_leather_boots():
    time.sleep(0.3)
    pyautogui.moveTo(1670, 2126) # select DARK leather macro
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(4.3) # wait for craft to complete


time.sleep(3) # startup pause
while True:
    craft_fine_leather_boots()