import pyautogui
import random
import os 

def macros(image_name_list : list, button_location_left_list : list, button_location_top_list : list, loop : bool):
    button_location = 0
    button_location_left_param = 0
    button_location_top_param = 0
    turn = 0 

    while turn < len(image_name_list):
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

        if turn == len(image_name_list) and loop == True:
            print("reset")
            turn = 0