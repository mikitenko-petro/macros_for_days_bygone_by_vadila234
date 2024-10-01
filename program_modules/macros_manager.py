import json
from .macros_setup import auto_rewind_manager
from .search_path import search_path

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
    process = 0

    while process < 10:
        with open(file = search_path('static/json/status.json'), encoding = 'utf-8', mode= 'r') as file:
            status = json.load(file)

        if status["status"] == "closed":
            with open(file = search_path('static/json/status.json'), encoding = 'utf-8', mode= 'w') as file:
                new_status = {"status": ""}
                json.dump(new_status, file)

            break

        if mode == "auto_rewind":
            print("auto_rewind")
            auto_rewind_manager(
            image_name_list = ["critical_damage","tree","rewind","rewind2","stats","tree","battle","campaing","start","back"],
            button_location_left_list = [500,"","","","",750,"","","",""],
            button_location_top_list = ["","",300,"","","","","","",""])

        elif mode == "elexir_master_farm":
            print("elexir_master_farm")
            auto_rewind_manager(
            image_name_list = ["critical_damage","tree","rewind","rewind2","elexir","ok","stats","tree","battle","campaing","start","back"],
            button_location_left_list = [500,"","","",700,"","",750,"","","",""],
            button_location_top_list = ["","",300,"","","","","","","","",""])

        else:
            print("stop")
            auto_rewind_manager([],[],[])

        process += 1

        if process == 10:
            process = 0
        