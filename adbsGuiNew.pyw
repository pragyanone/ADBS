import customtkinter as ctk
import tkinter as tk
from adbs import ad2bs, bs2ad
from datetime import datetime

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


def bs2adM(date):
    ctk.CTkLabel(root, text=date + " BS = " + bs2ad(date) + " AD").grid(columnspan=2)


def ad2bsM(date):
    ctk.CTkLabel(root, text=date + " AD = " + ad2bs(date) + " BS").grid(columnspan=2)


def clear():
    for widget in root.winfo_children():
        if type(widget) == ctk.CTkLabel:
            widget.grid_forget()


root = ctk.CTk()
root.title("ADBS")
root.resizable(0, 0)
clearButton = ctk.CTkButton(root, text="Clear", command=clear).grid(
    columnspan=2, sticky="e", padx=3, pady=3
)
bsDate = tk.StringVar()
adDate = tk.StringVar()
bsFrame = ctk.CTkFrame(root)
adFrame = ctk.CTkFrame(root)
bsFrame.grid(padx=5, pady=5)
adFrame.grid(padx=5, pady=5, row=1, column=1)
ctk.CTkLabel(bsFrame, text="BS date").grid()
ctk.CTkLabel(adFrame, text="AD date").grid()
bsDateEntry = ctk.CTkEntry(bsFrame, textvariable=bsDate)
bsDateEntry.insert(0, ad2bs(datetime.now().strftime("%Y-%m-%d")))
bsDateEntry.grid(padx=2)
bsDateEntry.bind("<Return>", lambda _: bs2adM(bsDate.get()))
adDateEntry = ctk.CTkEntry(adFrame, textvariable=adDate)
adDateEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))
adDateEntry.grid(padx=2)
adDateEntry.bind("<Return>", lambda _: ad2bsM(adDate.get()))
ctk.CTkButton(bsFrame, text="Convert to AD", command=lambda: bs2adM(bsDate.get())).grid(
    padx=5, pady=5
)
ctk.CTkButton(adFrame, text="Convert to BS", command=lambda: ad2bsM(adDate.get())).grid(
    padx=5, pady=5
)
root.mainloop()
