import json
import tkinter as tk


def action1():
    f = open('setting.json', 'r')
    data = json.load(f)
    f.close()
    fr.configure(width=data['w'], height=data['h'], background=data['col'])
    win.title(data['tit'])


win = tk.Tk()
fr = tk.Frame(master=win, width=280, height=180, background='olive')
fr.pack()
button = tk.Button(master=fr, text='Змінити вікно', width=15, height=2, command=action1)
button.place(x=75, y=65)
win.mainloop()