# macros_for_days_bygone_by_vadila234ua

_Мій проект - це один з можливих способів автоматизації повсякденних процесів, як ігрових так і більш серйозніших. Цей "Макрос" призначений для автоматизації ігрового процесу мобільної гри days bygone._

---

### DIFFERENT INFORMATION
- [Technologies, librares and languages І used](#technologies-librares-and-languages-і-used)
- [How use it](#how-use-it)

### How it works

- [Parallel Processing](#parallel-processing)
- [Grafical user interface](#grafical-user-interface)
- [Macros managing](#macros-managing)
- [Reading and clicking on screen](#reading-and-clicking-on-screen)
- [Searching path](#searching-path)
  
# Technologies librares and languages І used
1. >Python - I used Python for automatization and GUI.
2. >pyautogui - I used this Python library for screen trecking and clicking.
3. >customtkinter - I used this Python library for grafical UI.
4. >treading - I used this Python library for parallel processes.

---

# How use it
1. >git clone https://github.com/mikitenko-petro/macros_for_days_bygone_by_vadila234ua.git
2. >pip install -r requirements.txt
3. >python main.py
4. >install BlueStacks and days bygone
5. >pin days bygone icon on taskbar
6. >begin from stats screen and press button

---
# Parallel Processing

### process.py

1. __Using library threading for spliting main cycle and GUI because if we bind cycle and tkinter window will be freezed while macros is working__

```python
import threading
from program_modules.tkinter_setup import frame_start
from program_modules.macros_manager import macros_manager

frame = threading.Thread(target = frame_start)
macros = threading.Thread(target = macros_manager)

frame.start()
macros.start()

frame.join()
macros.join()

```

# Grafical user interface

### tkinter_setup.py

2. __Using library customtkinter for creating GUI__

```python
import customtkinter
import json
from .search_path import search_path
from .macros_manager import auto_rewind, elexir_master_farm, stop

class App(customtkinter.CTk):
    def __init__(self, title : str):
        super().__init__()

        self.title(title)
        self.geometry("600x600+1500+850")
        self.grid_columnconfigure((2,1),weight=1)
        self.iconbitmap(search_path("static/images/cosmetic/icon.ico"))
        self.attributes('-topmost',True)

        self.auto_rewind_button = customtkinter.CTkButton(self, text = "auto rewind", command = auto_rewind)
        self.auto_rewind_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.elexir_master_farm_button = customtkinter.CTkButton(self, text = "elexir master farm", command = elexir_master_farm)
        self.elexir_master_farm_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.stop_button = customtkinter.CTkButton(self, text = "stop", command = stop)
        self.stop_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.mainloop()

    def on_close(self):
        with open(file = search_path('static/json/status.json'), encoding = 'utf-8', mode= 'w') as file:
            status = {"status": "closed"}
            json.dump(status, file)
            
        self.destroy()

def frame_start():
    main = App(title = "macros_for_days_bygone_by_vadila234ua")
```

# Macros managing

### macros_manager.py

3. __creating main loop for managing which mode is using now__

```python
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
```

# reading and clicking on screen

### Macros_setup.py

4. __creating a function which searching for images and clicking on it in right turn. I use library pyautogui for this__

```python
import pyautogui
import random
from .capcha_swapper import capcha_swapper
from .search_path import search_path

turn = 0
is_capcha = False
current_image_name_list =[]

def auto_rewind_manager(image_name_list : list, button_location_left_list : list, button_location_top_list : list):
    global turn
    global is_capcha
    global current_image_name_list
    pyautogui.FAILSAFE = False

    if current_image_name_list != image_name_list:
        turn = 0
        current_image_name_list = image_name_list

    if turn == 0:
        try:
            capcha_location = pyautogui.locateOnScreen(search_path(f'static/images/images_to_find/exit2.png'), confidence=0.6)
            
            pyautogui.moveTo(
            capcha_location.left + capcha_location.width/2 + random.randint(-3, 3),
            capcha_location.top + capcha_location.height/2 + random.randint(-3, 3))

            pyautogui.click()
            is_capcha = True
        except:
            is_capcha = False

        try:
            capcha_location = pyautogui.locateOnScreen(search_path(f'static/images/capcha_images/select.png'), confidence=0.8)
            capcha_swapper()
            is_capcha = True
        except:
            is_capcha = False
        
        try:
            capcha_location = pyautogui.locateOnScreen(search_path(f'static/images/capcha_images/tap.png'), confidence=0.7)
            capcha_swapper()
            is_capcha = True
        except:
            is_capcha = False
        
    if is_capcha == False:
        try:
            button_location = pyautogui.locateOnScreen(search_path(f"static/images/images_to_find/{image_name_list[turn]}.png"), confidence=0.9)
            
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
        turn = 0
```

# Searching path

### search_path.py

5. __creating a function which make dynamic path to files(photos, json)__

```python
import os

def search_path(file_name: str):
    base_path = os.path.abspath(".")
    path = os.path.join(base_path, file_name)
    return path
```
