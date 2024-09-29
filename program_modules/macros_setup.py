import pyautogui
import random
from .capcha_swapper import capcha_swapper
from .search_path import search_path

def auto_rewind_manager(image_name_list : list, button_location_left_list : list, button_location_top_list : list):
    button_location = 0
    button_location_left_param = 0
    button_location_top_param = 0
    turn = 0
    is_capcha = False
    pyautogui.FAILSAFE = False

    while turn < len(image_name_list):
        if turn == 0:
            try:
                capcha_location = pyautogui.locateOnScreen(search_path(f'images/images_to_find/exit2.png'), confidence=0.6)
                
                pyautogui.moveTo(
                capcha_location.left + capcha_location.width/2 + random.randint(-3, 3),
                capcha_location.top + capcha_location.height/2 + random.randint(-3, 3))

                pyautogui.click()
                is_capcha = True
            except:
                is_capcha = False

            try:
                capcha_location = pyautogui.locateOnScreen(search_path(f'images/capcha_images/select.png'), confidence=0.8)
                capcha_swapper()
                is_capcha = True
            except:
                is_capcha = False
            
            try:
                capcha_location = pyautogui.locateOnScreen(search_path(f'images/capcha_images/tap.png'), confidence=0.7)
                capcha_swapper()
                is_capcha = True
            except:
                is_capcha = False
            
        if is_capcha == False:
            try:
                button_location = pyautogui.locateOnScreen(search_path(f"images/images_to_find/{image_name_list[turn]}.png"), confidence=0.9)
                
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