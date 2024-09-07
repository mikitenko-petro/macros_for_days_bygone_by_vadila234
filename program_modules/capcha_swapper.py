import pyautogui
import os
import random
from .macros import macros

def capcha_swapper():
    image_name_list = ["exit","close","icon","expand","play","play"]
    location_left_list = ["","","","","",""]
    location_top_list = ["","","","","",""]

    macros(image_name_list, location_left_list, location_top_list, False)