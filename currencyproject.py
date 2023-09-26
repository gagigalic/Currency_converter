import requests
import customtkinter
from tkinter import *

base_url = "https://v6.exchangerate-api.com/v6/20267e87612d56bbe6c3473f/latest/"
response = requests.get(base_url + "BAM")
data = response.json()
choice = list(data['conversion_rates'])


def convert_currency():

    amount = int(amount_entry.get())
    from_currency = from_currency_choice.get()
    to_currency = to_currency_choice.get()

    if 'conversion_rates' in data:
        rates = data['conversion_rates']
        if from_currency == to_currency:
            change_label(amount)

        if from_currency in rates and to_currency in rates:
            conversion_rate = rates[to_currency] / rates[from_currency]
            converted_amount = round(amount * conversion_rate,4)

            change_label(converted_amount)
            return converted_amount
        else:
            raise ValueError("Invalid currency!")
    else:
        raise ValueError("Unable to fetch exchange rates!")


def change_label(result):
    result="Result: "+str(result)
    result_label.configure(text = result)

def reset():
    result_label.configure(text = "")
    from_currency_choice.set("")
    to_currency_choice.set("")
    amount_entry.delete(0, 'end')

def close ():
    app.destroy()

app = customtkinter.CTk()
app.config(bg = "#4682A9")
app.geometry("600x450")
app.title("Currency Converter")
app.resizable(False, False)

font1 = ("Arial", 25, "bold")
font2 = ("Arial", 20, "bold")

title = customtkinter.CTkLabel(app, font=font1, text="Welcome to Real Time Currency Converter", text_color="#fff", bg_color="#4682A9")
title.place(x=50, y=80)

variable1 = StringVar()
variable2 = StringVar()

from_currency_choice = customtkinter.CTkComboBox(app, font = font2, text_color= "#000", fg_color="#fff", dropdown_hover_color= "#0C9295", button_color="#4682A9", button_hover_color="#0C9295", border_color="#0C9295", width=180, variable=variable1, values=choice, state="readonly")
from_currency_choice.place(x = 50, y = 180)

amount_entry = customtkinter.CTkEntry(app, font=font2, text_color="#000", bg_color="#161C25", border_color="#0C9295",border_width=2, width=180)
amount_entry.place(x=200, y=230)

to_currency_choice = customtkinter.CTkComboBox(app, font = font2, text_color= "#000", fg_color="#fff", dropdown_hover_color= "#0C9295", button_color="#4682A9", button_hover_color="#0C9295", border_color="#0C9295", width=180, variable=variable2, values=choice, state="readonly")
to_currency_choice.place(x = 350, y = 180)

convert_button = customtkinter.CTkButton(app, command = convert_currency,  font=font2, text_color="#fff", text="Convert",
                                             fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor="hand2",
                                             corner_radius=15, width=150)
convert_button.place(x=100, y=280)

reset_button = customtkinter.CTkButton(app, command = reset,  font=font2, text_color="#fff", text="Reset",
                                             fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor="hand2",
                                             corner_radius=15, width=150)
reset_button.place(x=320, y=280)

result_label = customtkinter.CTkLabel(app, font=font2, text="", text_color="#fff", bg_color="#4682A9")
result_label.place(x=180, y=330)

quit_button = customtkinter.CTkButton(app, command = close,  font=font2, text_color="#fff", text="Quit",
                                             fg_color= "#164B60", hover_color= "#749BC2", bg_color="#4682A9", cursor="hand2",
                                             corner_radius=15, width=150)
quit_button.place(x=210, y=370)

app.mainloop()


