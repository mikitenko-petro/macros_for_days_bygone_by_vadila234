import tkinter
from program_modules.macros_setup import auto_rewind_manager

image_name_list = ["tree","rewind","rewind2","stats","damage","battle","campaing","start","back"]
location_left_list = ["","","","",600,"","",-200,""]
location_top_list = ["",300,"","","","","","",""]

def test_button(root):
    button = tkinter.Button(
        master = root,
        text = "test rewind",
        width = 25,
        command = lambda: auto_rewind_manager(image_name_list, location_left_list, location_top_list))
    
    return button
