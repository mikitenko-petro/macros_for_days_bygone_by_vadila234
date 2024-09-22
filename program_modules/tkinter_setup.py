import tkinter
from .buttons.rewind_button import rewind_button
from .buttons.elexir_master_button import elexir_master_button
from .search_image import search_image
from PIL import Image, ImageTk

main = tkinter.Tk()
main.title("macros_for_days_bygone_by_vadila234ua")
main.geometry("600x600+1500+850")
main.minsize(600,600)
main.maxsize(600,600)
main.attributes('-topmost',True)
main.iconphoto(False, ImageTk.PhotoImage(Image.open(search_image("images/cosmetic/icon.png"))))

button = rewind_button(main)
button.place(x = 200,y = 50)

button2 = elexir_master_button(main)
button2.place(x = 200,y = 100)


main.mainloop()