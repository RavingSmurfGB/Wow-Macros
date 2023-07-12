import pyautogui, time

# How to use
# Search your item you wants lots of
# Click on Current Bid so Arrow Points up - means by biggest stack generally
# Start script
# Be sure to Drag mouse to the top left corner when you want to stop
# 478 525

def buy_searched_item():
    time.sleep(0.05)
    pyautogui.moveTo(478, 525) # Click iten
    time.sleep(0.05)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.05)
    pyautogui.moveTo(1605, 1194) # Click Buyout
    time.sleep(0.05)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()
    time.sleep(0.05)
    pyautogui.moveTo(1762, 443) # Click accept
    time.sleep(0.05)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()



time.sleep(3) # startup pause
while True:
    buy_searched_item()