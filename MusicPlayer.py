import tkinter as tk
import pygame as pg

root = tk.Tk()
root.title("Music Player")
root.geometry("600x400")  # size of window
root.resizable(0, 0)  # user cant resize window


# --------- song play list ---------

# --------- song Track ---------
trackframe = tk.LabelFrame(
    root, text="Song Track", bg="black", fg="white", bd=5, font=("arial", 10)
)
trackframe.place(x=10, y=0, width=580, height=90)


ShowSongName = tk.Text(
    trackframe, bg="white", fg="black", width=50, height=1, state="disabled"
)
ShowSongName.grid(row=0, column=0, padx=17, pady=13)

ShowStatus = tk.Label(trackframe, bg="white", fg="black", width=15)
ShowStatus.grid(row=0, column=1)

# --------- control panel ---------

root.mainloop()
