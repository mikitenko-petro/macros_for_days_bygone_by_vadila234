# macros_for_days_bygone_by_vadila234ua

_My project is one of the possible ways to automazate everyday processes, both playful and more serious. This "Macros" is designed to automate the gameplay of the mobile game days bygone._ <br />
_Мій проект - це один з можливих способів автоматизації повсякденних процесів, як ігрових так і більш серйозніших. Цей "Макрос" призначений для автоматизації ігрового процесу мобільної гри days bygone._ <br />

---

### DIFFERENT INFORMATION
- [Technologies, librares and languages І used](#technologies-librares-and-languages-і-used)
- [How use it](#how-use-it)
- [Conclusion](#conclusion)

### How it works

- [Parallel Processing](#parallel-processing)
- [Grafical user interface](#grafical-user-interface)
- [Macros managing](#macros-managing)
- [Reading and clicking on screen](#reading-and-clicking-on-screen)
- [Searching path](#searching-path)
  
# Technologies librares and languages І used
1. >Python - I used Python for automatization and GUI. <br />
   >Я використовував Python для автоматизації та інтерфейсу.<br />
2. >pyautogui - I used this Python library for screen trecking and clicking. <br />
   >Я використовував цю бібліотеку Python для відстеження та клацання по екрану. <br />
3. >customtkinter - I used this Python library for grafical UI. <br />
   >Я використовував цю бібліотеку Python для графічного інтерфейсу. <br />
4. >treading - I used this Python library for parallel processes. <br />
   >Я використовував цю бібліотеку Python для паралельних процесів. <br />

---

# How use it
### console
1. >git clone https://github.com/mikitenko-petro/macros_for_days_bygone_by_vadila234ua.git
2. >pip install -r requirements.txt
3. >python main.py
### installing emulator
4. >install BlueStacks and days bygone
5. >pin days bygone icon on taskbar
6. >begin from stats screen and press button

---
# Parallel Processing

### process.py

1. __Using library threading for spliting main cycle and GUI because if we bind cycle and tkinter window will be freezed while macros is working__ <br />
   __Використання бібліотеки threading для розділення основного циклу та графічного інтерфейсу користувача, оскільки якщо ми прив’яжемо цикл і вікно tkinter то воно буде заморожено, поки макрос працює__ <br />

```python
import threading
from program_modules.tkinter_setup import frame_start
from program_modules.macros_manager import macros_manager

frame = threading.Thread(target = frame_start) # оголшуемо змінні процесів
macros = threading.Thread(target = macros_manager)

frame.start() # запускаємо процеси
macros.start()

frame.join() # використовуємо метод join щоб дати гарантію того що запущені процеси будуть завершені коли файл припине працювати
macros.join()

```

# Grafical user interface

### tkinter_setup.py

2. __Using library customtkinter for creating GUI__ <br />
   __Використання бібліотеки customtkinter для створення GUI__ <br />

```python
import customtkinter
import json
from .search_path import search_path
from .macros_manager import auto_rewind, elexir_master_farm, stop

class App(customtkinter.CTk): # оголошуемо клас який налідуе клас вікна
    def __init__(self, title : str):
        super().__init__()

        self.title(title) # робимо налаштування вікна
        self.geometry("600x600+1500+850")
        self.grid_columnconfigure((2,1),weight=1)
        self.iconbitmap(search_path("static/images/cosmetic/icon.ico"))
        self.attributes('-topmost',True) # цей параметр відповідае за те що вікно буде відображатися поверх інших

        self.auto_rewind_button = customtkinter.CTkButton(self, text = "auto rewind", command = auto_rewind) # оголошуемо кнопки які відповідають за зміну режима макроса
        self.auto_rewind_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.elexir_master_farm_button = customtkinter.CTkButton(self, text = "elexir master farm", command = elexir_master_farm)
        self.elexir_master_farm_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.stop_button = customtkinter.CTkButton(self, text = "stop", command = stop)
        self.stop_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        self.protocol("WM_DELETE_WINDOW", self.on_close) # прописуемо дії які будуть виконуватися при закриванні вікна

        self.mainloop()

    def on_close(self):
        with open(file = search_path('static/json/status.json'), encoding = 'utf-8', mode= 'w') as file: # перезаписуемо статус вікна у json як назалежний файл оскілки це набагато легше ніж намагатися читати стаус вікна беспосередньо у пайтоні
            status = {"status": "closed"}
            json.dump(status, file)
            
        self.destroy()

def frame_start(): #оголошуемо функцію запуску вікна
    main = App(title = "macros_for_days_bygone_by_vadila234ua")
```

# Macros managing

### macros_manager.py

3. __Сreating main loop for managing which mode is using now__ <br />
   __Створення основного циклу для керування тим, який режим зараз використовується__ <br />

```python
import json
from .macros_setup import auto_rewind_manager
from .search_path import search_path

mode = "" # оголошення змінної режиму

def stop(): # функції для зміни режимів
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

    while process < 10: # створення циклу який постійно викликає основну функцію
        with open(file = search_path('static/json/status.json'), encoding = 'utf-8', mode= 'r') as file: # зчитування файлу json для розуміння чи закрите вікно
            status = json.load(file)

        if status["status"] == "closed": # якщо вікно закрите то перезаписати статус та завершити цикл
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

        if process == 10: # анулювання кількості циклів для коректної роботи
            process = 0
```

# reading and clicking on screen

### Macros_setup.py

4. __creating a function which searching for images and clicking on it in right turn. I use library pyautogui for this__ <br />
   __створення функції, яка шукає зображення та натискає на нього у потрібний момент. Для цього я використовую бібліотеку pyautogui__ <br />

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
    pyautogui.FAILSAFE = False # відключення перевірки на те що курсор на краю екрану оскільки може видавати помилку

    if current_image_name_list != image_name_list: # анулюемо чергу якщо змінюемо режим
        turn = 0
        current_image_name_list = image_name_list

    if turn == 0: # якщо нульова черга то перевіряемо на наявність капчі та хрестика
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
        try: # якщо не знаходить зображення то видає помилку, тому обов'язково використовуемо страховку
            button_location = pyautogui.locateOnScreen(search_path(f"static/images/images_to_find/{image_name_list[turn]}.png"), confidence=0.9) # передаемо функції шлях до фото яке треба знайти, параметр confidence відповідае за розпізнавання зображення при похибці
            if button_location_left_list[turn] == "":
                button_location_left_param = button_location.width/2
            else:
                button_location_left_param = button_location_left_list[turn]

            if button_location_top_list[turn] == "":
                button_location_top_param = button_location.height/2
            else:
                button_location_top_param = button_location_top_list[turn]

            pyautogui.moveTo( # переміщення курсора до координат з невеликим відхиленням
            button_location.left + button_location_left_param + random.randint(-3, 3),
            button_location.top + button_location_top_param + random.randint(-3, 3))

            pyautogui.click() # клікаемо
            
            turn += 1 # переходимо до слідучої черги
            print(turn)
        except:
            pass

    if turn == len(image_name_list): # якщо зображень більше немае то анульовуємо чергу
       turn = 0
```

# Searching path

### search_path.py

5. __creating a function which make dynamic path to files(photos, json)__ <br />
   __створення функції, яка створює динамічний шлях до файлів (фото, json)__ <br />

```python
import os

def search_path(file_name: str):
    base_path = os.path.abspath(".") # шлях до кореневої папки проекту
    path = os.path.join(base_path, file_name)
    return path
```

---

# Conclusion

_working with this project, you will get the skills of working with multithreading, developing a graphic interface, reading and interacting with the screen, working with json, finding the right path to files._ <br />
_працюючи з цим проектом ви отримайте навички роботи з багатопоточністю, розробки графічного інтерфейсу, зчитуванням та взаемодією з екраном, роботою з json, правильним знаходженням шляху до файлів._
