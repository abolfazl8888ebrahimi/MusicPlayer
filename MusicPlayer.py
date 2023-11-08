import tkinter as tk
import pygame as pg

root = tk.Tk()
root.title("Music Player")
root.geometry("600x400")  # size of window
root.resizable(0, 0)  # user cant resize window


# --------- song play list ---------

SongFrame = tk.LabelFrame(
    root, text="Song Play List", bg="black", fg="white", bd=5, font=("arial", 10)
)
SongFrame.place(x=10, y=1, width=580, height=210)
Scrolly = tk.Scrollbar(SongFrame, orient="vertical")
PlayList = tk.Listbox(
    SongFrame,
    bg="silver",
    fg="black",
    font=("Arial", 5),
    selectmode="single",
    selectbackground="black",
    height=100,
)
Scrolly.config(command=PlayList.yview)
Scrolly.pack(fill="y", side="right")
PlayList.pack(fill="both")


# --------- song Track ---------
trackframe = tk.LabelFrame(
    root, text="Song Track", bg="black", fg="white", bd=5, font=("arial", 10)
)
trackframe.place(x=10, y=214, width=580, height=90)


ShowSongName = tk.Text(
    trackframe, bg="white", fg="black", width=50, height=1, state="disabled"
)
ShowSongName.grid(row=0, column=0, padx=17, pady=13)

ShowStatus = tk.Label(trackframe, bg="white", fg="black", width=15)
ShowStatus.grid(row=0, column=1)

# --------- control panel ---------

CtrPanel = tk.LabelFrame(
    root, text="Contro Panel", bg="black", fg="white", bd=5, font=("arial", 10), padx=15
)
CtrPanel.place(x=10, y=308, width=580, height=90)

PlayBtn = tk.Button(CtrPanel, text="play", width=15)
PlayBtn.grid(row=0, column=0, padx=10, pady=17)

StopBtn = tk.Button(CtrPanel, text="Stop", width=15)
StopBtn.grid(row=0, column=1, padx=10, pady=17)

UnpuaseBtn = tk.Button(CtrPanel, text="Unpuasing", width=15)
UnpuaseBtn.grid(row=0, column=2, padx=10, pady=17)

PuaseBtn = tk.Button(CtrPanel, text="Puase", width=15)
PuaseBtn.grid(row=0, column=3, padx=10, pady=17)
root.mainloop()
