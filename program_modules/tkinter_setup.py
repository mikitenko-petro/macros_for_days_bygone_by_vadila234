import tkinter
from .buttons.rewind_button import rewind_button
from .buttons.elexir_master_button import elexir_master_button
from .buttons.test_button import test_button

main = tkinter.Tk()
main.title("macros_for_days_bygone_by_vadila234ua")
main.geometry("600x600+1500+850")
main.minsize(600,600)
main.maxsize(600,600)
main.attributes('-topmost',True)

button = rewind_button(main)
button.place(x = 200,y = 50)

button2 = elexir_master_button(main)
button2.place(x = 200,y = 100)

# button3 = test_button(main)
# button3.place(x = 200,y = 150)


main.mainloop()