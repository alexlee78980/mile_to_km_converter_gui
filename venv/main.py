import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=10,pady=10)
text = tkinter.Entry(width=10)
text.grid(column=1,row = 0)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

is_equal_to =tkinter.Label(text="is equal to")
is_equal_to.grid(column=0,row=1)

km_value = tkinter.Label(text="0")
km_value.grid(column=1,row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2,row=1)
def button_clicked():
     km_value["text"] = str(int(text.get()) * 1.60934)
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()