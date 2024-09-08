from .macros import macros

def capcha_swapper():
    image_name_list = ["exit","close","icon","expand","play"]
    location_left_list = ["","","","","",""]
    location_top_list = ["","","","","",""]
    print("trying to swap")
    macros(image_name_list, location_left_list, location_top_list, False)
    print("swap complete")
