import pyautogui, time







# location 
# 1570 2126
def craft_fine_leather_boots():
    time.sleep(0.3)
    pyautogui.moveTo(1570, 2126) # select fine leather macro
    time.sleep(0.3)
    pyautogui.click()
    time.sleep(4.2) # wait for craft to complete


time.sleep(3) # startup pause
while True:
    craft_fine_leather_boots()