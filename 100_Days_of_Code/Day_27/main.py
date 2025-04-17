from tkinter import *

def button_clicked():
    miles = float(miles_input.get())
    km = round(miles*1.609344)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)

#Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

#Label
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

#Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

#Label
km_result_label= Label(text="0")
km_result_label.grid(column=1, row=1)

#Label
Km_label = Label(text="Km")
Km_label.grid(column=3, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()