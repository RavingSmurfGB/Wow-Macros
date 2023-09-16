import pyautogui, time


# while True:
#     time.sleep(1)
#     currentMouseX, currentMouseY = pyautogui.position() 
#     print (currentMouseX, currentMouseY)




def get_mail():
    # Mail 119 474
    # mail item 1256 1115
    # mail delete 1373 1201
    time.sleep(0.05)
    pyautogui.moveTo(119, 474) # select mail item
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.05)
    pyautogui.moveTo(1256, 1115) # get mail attachment
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.05)
    pyautogui.moveTo(1373, 1201)
    time.sleep(0.05)
    pyautogui.click()
    time.sleep(0.05)

    #pyautogui.click(1373, 1201) # Delete mail - not used when getting attachment




time.sleep(3) # startup pause
while True:
    get_mail()
    # with py auto gui we can search the screen for a screen shot - I do that to list items yesh:)
    





