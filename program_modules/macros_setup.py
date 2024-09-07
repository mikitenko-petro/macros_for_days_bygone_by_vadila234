import pyautogui
import random
from .capcha_swapper import capcha_swapper
import os 

test = False
make_screenshoots = False

def auto_rewind_manager(image_name_list : list, button_location_left_list : list, button_location_top_list : list, root):
    button_location = 0
    button_location_left_param = 0
    button_location_top_param = 0
    turn = 0
    is_capcha = ""

    while turn < len(image_name_list):
        if turn == 0:
            try:
                capcha_location = pyautogui.locateOnScreen(os.path.abspath(f'images/capcha_images/select.png'), confidence=0.5)
                capcha_swapper()
            except:
                is_capcha = ""
            
            try:
                capcha_location = pyautogui.locateOnScreen(os.path.abspath(f'images/capcha_images/tap_circles.png'), confidence=0.5)
                capcha_swapper()
                is_capcha = "tap circles"
            except:
                is_capcha = ""
            
            try:
                capcha_location = pyautogui.locateOnScreen(os.path.abspath(f'images/capcha_images/tap_items.png'), confidence=0.5)
                capcha_swapper()
                is_capcha = "tap items"
            except:
                is_capcha = ""
        
        if is_capcha == "":
            try:
                button_location = pyautogui.locateOnScreen(os.path.abspath(f"images/images_to_find/{image_name_list[turn]}.png"), confidence=0.9)
                
                if button_location_left_list[turn] == "":
                    button_location_left_param = button_location.width/2
                else:
                    button_location_left_param = button_location_left_list[turn]

                if button_location_top_list[turn] == "":
                    button_location_top_param = button_location.height/2
                else:
                    button_location_top_param = button_location_top_list[turn]

                pyautogui.moveTo(
                button_location.left + button_location_left_param + random.randint(-3, 3),
                button_location.top + button_location_top_param + random.randint(-3, 3))

                pyautogui.click()
                
                turn += 1
                print(turn)
            except:
                pass

        if turn == len(image_name_list):
            print("reset")
            turn = 0