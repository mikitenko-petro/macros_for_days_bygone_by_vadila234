import tkinter
from program_modules.macros_setup import auto_rewind_manager

image_name_list = ["critical_damage","tree","rewind","rewind2","stats","tree","battle","campaing","start","back"]
location_left_list = [500,"","","","",750,"","","",""]
location_top_list = ["","",300,"","","","","","",""]

def rewind_button(root):
    button = tkinter.Button(
        master = root,
        text = "auto rewind",
        width = 25,
        command = lambda: auto_rewind_manager(image_name_list, location_left_list, location_top_list, root))
    
    return button





