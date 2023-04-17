import customtkinter
import tkinter
from tkinter import messagebox
import os
import sys

#FUNCIONES
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def calculadora():
    try:
        regla_de_3 = (100*valor_a_aproximar.get())/(valor_del_cien.get())
        regla_de_3=("{:.2f}".format(regla_de_3))
        label = customtkinter.CTkLabel(text=str(regla_de_3)+"%",text_font=("Roboto Black",32),anchor="e", text_color=("#2980B9"),width=180)
        label.place(relx=0.53,y=120+a)
    except:
        messagebox.showinfo(message="Al parecer ingresaste valores no válidos amor", title="Error")

def calcular():
    try:
        regla_de_3 = ((valor_del_cien_2.get())*valor_a_aproximar_2.get())/100

        regla_de_3=("{:.2f}".format(regla_de_3))
        label = customtkinter.CTkLabel(text=str(regla_de_3)+"pts",text_font=("Roboto Black",32),anchor="e", text_color=("#2980B9"),width=180)
        label.place(relx=0.53,y=120+b)
    except:
        messagebox.showinfo(message="Al parecer ingresaste valores no válidos amor", title="Error")

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
ancho_ventana = int(600)
alto_ventana = int(390*1.4)

x_ventana = app.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = app.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana-30)
app.geometry(posicion)
app.title("Calculadora de Notas")
iconPath = resource_path("Logo.ico")
app.iconbitmap(iconPath)
app.resizable(0,0)

#TEXTOS 1
a=20
label = customtkinter.CTkLabel(text="Nota total",text_font=("Roboto Black",18),anchor="w")
label.place(relx=0.05,y=20+a)

label = customtkinter.CTkLabel(text="Nota a calcular",text_font=("Roboto Black",18),anchor="w")
label.place(relx=0.05,y=100+a)

label = customtkinter.CTkLabel(text="=",text_font=("Roboto Black",38),anchor="w", text_color=("#2980B9"))
label.place(relx=0.47,y=35+a)
label = customtkinter.CTkLabel(text="=",text_font=("Roboto Black",38),anchor="w", text_color=("#2980B9"))
label.place(relx=0.47,y=115+a)

label = customtkinter.CTkLabel(text="100%",text_font=("Roboto Black",32),anchor="e", text_color=("#2980B9"),width=180)
label.place(relx=0.53,y=40+a)


#ENTRYS 1
valor_del_cien = tkinter.IntVar()
valor_del_cien_entry = customtkinter.CTkEntry(master=app,textvariable=valor_del_cien, justify="left")
valor_del_cien_entry.config(width=45)
valor_del_cien_entry.place(relx=0.05,y=60+a)

valor_a_aproximar = tkinter.IntVar()
valor_a_aproximar_entry = customtkinter.CTkEntry(master=app,textvariable=valor_a_aproximar, justify="left")
valor_a_aproximar_entry.config(width=45)
valor_a_aproximar_entry.place(relx=0.05,y=140+a)

#TEXTOS 2
b=290
label = customtkinter.CTkLabel(text="Nota total",text_font=("Roboto Black",18),anchor="w")
label.place(relx=0.05,y=20+b)

label = customtkinter.CTkLabel(text="Porcentaje a calcular",text_font=("Roboto Black",18),anchor="w")
label.place(relx=0.05,y=100+b)

label = customtkinter.CTkLabel(text="=",text_font=("Roboto Black",38),anchor="w", text_color=("#2980B9"))
label.place(relx=0.47,y=35+b)
label = customtkinter.CTkLabel(text="=",text_font=("Roboto Black",38),anchor="w", text_color=("#2980B9"))
label.place(relx=0.47,y=115+b)

label = customtkinter.CTkLabel(text="100%",text_font=("Roboto Black",32),anchor="e", text_color=("#2980B9"),width=180)
label.place(relx=0.53,y=40+b)


#ENTRYS 2
valor_del_cien_2 = tkinter.IntVar()
valor_del_cien_2_entry = customtkinter.CTkEntry(master=app,textvariable=valor_del_cien_2, justify="left")
valor_del_cien_2_entry.config(width=45)
valor_del_cien_2_entry.place(relx=0.05,y=60+b)

valor_a_aproximar_2 = tkinter.IntVar()
valor_a_aproximar_2_entry = customtkinter.CTkEntry(master=app,textvariable=valor_a_aproximar_2, justify="left")
valor_a_aproximar_2_entry.config(width=45)
valor_a_aproximar_2_entry.place(relx=0.05,y=140+b)

#BOTONES

button = customtkinter.CTkButton(master=app, text="Calcular",text_font=("Roboto Bold",12), compound="bottom",command=calculadora)
button.place(relx=0.57, rely=0.42)

button = customtkinter.CTkButton(master=app, text="Calcular",text_font=("Roboto Bold",12), compound="bottom",command=calcular)
button.place(relx=0.57, rely=0.90)


app.mainloop()