'Used for wow TBC 2.4.3 to stop going AFK'
import pyautogui, random, time



while True:

    delay = random.randint(1, 9)
    print("Waiting for - " + str(delay))
    time.sleep(delay)
    pyautogui.keyDown('w')

    delay = random.randint(1, 9)
    print("Waiting for - " + str(delay))
    time.sleep(delay)
    pyautogui.keyUp('w')