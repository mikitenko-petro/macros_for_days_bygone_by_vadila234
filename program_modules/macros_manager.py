from .macros_setup import auto_rewind_manager

mode = ""

def stop():
    global mode
    mode = ""

def auto_rewind():
    global mode
    mode = "auto_rewind"

def elexir_master_farm():
    global mode
    mode = "elexir_master_farm"

def macros_manager():
    global mode
    current_mode = ""
    process = 0

    while process < 10:
        if mode == "auto_rewind" and current_mode != mode:
            print("auto_rewind")
            auto_rewind_manager(
            image_name_list = ["critical_damage","tree","rewind","rewind2","stats","tree","battle","campaing","start","back"],
            button_location_left_list = [500,"","","","",750,"","","",""],
            button_location_top_list = ["","",300,"","","","","","",""])

            current_mode = mode

        elif mode == "elexir_master_farm" and current_mode != mode:
            print("elexir_master_farm")
            auto_rewind_manager(
            image_name_list = ["critical_damage","tree","rewind","rewind2","elexir","ok","stats","tree","battle","campaing","start","back"],
            button_location_left_list = [500,"","","",700,"","",750,"","","",""],
            button_location_top_list = ["","",300,"","","","","","","","",""])

            current_mode = mode

        elif mode == "" and current_mode != mode:
            print("stop")
            auto_rewind_manager([],[],[])
            current_mode = mode

        if process == 10:
            process = 0
