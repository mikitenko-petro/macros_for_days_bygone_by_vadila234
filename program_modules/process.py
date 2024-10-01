import threading
from program_modules.tkinter_setup import frame_start
from program_modules.macros_manager import macros_manager

frame = threading.Thread(target = frame_start)
macros = threading.Thread(target = macros_manager)

frame.start()
macros.start()

frame.join()
macros.join()

