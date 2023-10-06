# Парадигмы: императивная структурная, процедурная, ООП

import tkinter as tk
count = 0
count_run = False

class Timer():
    def __init__(self, win, label):
        self.root = win
        self.label = label

        self.updateClock()
        self.root.mainloop()

    def updateClock(self):
        global count, count_run
        if count_run:
            count += 1
        self.label.configure(text=count)
        self.root.after(1000, self.updateClock)


def click_start():
    global count, count_run
    count = 0
    count_run = True


def click_pause():
    global count_run
    count_run = False


def click_resume():
    global count_run
    count_run = True


def click_stop():
    global count, count_run
    count = 0
    count_run = False


win = tk.Tk()
win.title('Timer')
win.geometry('300x200')

label = tk.Label(text="", font=('Times New Roman', 40))
label.grid(column=2, row=0)

start_btn = tk.Button(text="Start", padx=5, pady=5, command=click_start)
start_btn.grid(column=0, row=1)

pause_btn = tk.Button(text="Pause", padx=5, pady=5, command=click_pause)
pause_btn.grid(column=1, row=1)

resume_btn = tk.Button(text="Resume", padx=5, pady=5, command=click_resume)
resume_btn.grid(column=2, row=1)

stop_btn = tk.Button(text="Stop", padx=5, pady=5, command=click_stop)
stop_btn.grid(column=3, row=1)

timer = Timer(win, label)



