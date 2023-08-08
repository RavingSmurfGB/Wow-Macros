import time, pyautogui


## How To Use:
# Go To Auction house
# Open Auction House
# Open Auctions Tab
# Drag in first item and price it
# Press Create
# It will then list your entire inventory by dragging in every slot...
# Be sure to Drag mouse to the top left corner of screen once everything is listed



#3165 1281
original_slot_location = [3210, 1194]# THIS IS LOCATION OF MY FIRST INVENTORY SLOT I want to craft from
# from this we fugre out all the other slots :)
bag_width = 7



def select_from_bag(location):
    time.sleep(0.1)
    pyautogui.moveTo(location) # select fine leather macro
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(0.1) 

def place_into_auction_house():
    time.sleep(0.1)
    pyautogui.moveTo(87 ,453)
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.1) 

def create_auction():
    time.sleep(0.1)
    pyautogui.moveTo(266, 1037)#266 1037
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1) 
    

time.sleep(3) # startup pause



new_slot_location = original_slot_location
bag_slot_current = 0
while True:

    if bag_slot_current < 8:
        bag_slot_current = bag_slot_current + 1
        #Move right
        print("BACK SLOT = " , bag_slot_current)
        
        select_from_bag(new_slot_location)
        place_into_auction_house()
        create_auction()
        new_slot_location[0] += 88 # move width axis along to the right by ..

    else:
        new_slot_location[0] = 3163 # Set Width axis back to orignal -- HAVE TO HARD CODE THIS :( TO FIRST SLOT AXIS 1
        new_slot_location[1] += 88 # move Lenth axis down by ..
        bag_slot_current = 0
        