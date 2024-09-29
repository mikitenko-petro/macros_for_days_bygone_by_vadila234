import program_modules
import threading
from program_modules.GUI.tkinter_setup import frame_start
from program_modules.macros_manager import macros_manager

if __name__ == "__main__":
    frame = threading.Thread(target = frame_start)
    macros = threading.Thread(target = macros_manager)

    frame.start()
    macros.start()

    frame.join()
    macros.join()
