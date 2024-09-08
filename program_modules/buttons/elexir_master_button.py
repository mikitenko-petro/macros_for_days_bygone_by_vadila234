import tkinter
from program_modules.macros_setup import auto_rewind_manager

image_name_list = ["critical_damage","tree","rewind","rewind2","elexir","ok","stats","tree","battle","campaing","start","back"]
location_left_list = [500,"","","",700,"","",750,"","","",""]
location_top_list = ["","",300,"","","","","","","","",""]

def elexir_master_button(root):
    button = tkinter.Button(
        master = root,
        text = "elexir master farm",
        width = 25,
        command = lambda: auto_rewind_manager(image_name_list, location_left_list, location_top_list))
    
    return button
