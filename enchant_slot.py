import pyautogui, time

# How to use
# Search your item you wants lots of
# Click on Current Bid so Arrow Points up - means by biggest stack generally
# Start script
# Be sure to Drag mouse to the top left corner when you want to stop
# 478 525




def buy_searched_item():
    time.sleep(0.05)
    pyautogui.moveTo(1151, 1094) # Click enchant button
    time.sleep(0.05)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.05)
    pyautogui.moveTo(3247, 1215) # Click item
    time.sleep(0.05)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.05)
    pyautogui.moveTo(1776, 413) # Click replace enchant
    time.sleep(0.05)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(4.5) # wait for enchance



time.sleep(3) # startup pause
while True:
    buy_searched_item()