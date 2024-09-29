import customtkinter
from ..search_path import search_path
from ..macros_manager import auto_rewind, elexir_master_farm, stop

class App(customtkinter.CTk):
    def __init__(self, title : str):
        super().__init__()

        self.title(title)
        self.geometry("600x600+1500+850")
        self.grid_columnconfigure((2,1),weight=1)
        self.iconbitmap(search_path("images/cosmetic/icon.ico"))
        self.attributes('-topmost',True)

        self.auto_rewind_button = customtkinter.CTkButton(self, text = "auto rewind", command = auto_rewind)
        self.auto_rewind_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.elexir_master_farm_button = customtkinter.CTkButton(self, text = "elexir master farm", command = elexir_master_farm)
        self.elexir_master_farm_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.stop_button = customtkinter.CTkButton(self, text = "stop", command = stop)
        self.stop_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew")