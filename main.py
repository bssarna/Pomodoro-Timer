#218, 219
from tkinter import *
import math

#constants
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MINS = 120
BREAK_MINS = 10
#120-10-120-15-120-20-120

window = Tk()
window.title("Session Timer")

#main canvas
canvas = Canvas(width=626, height=417)
img = PhotoImage(file="image.gif")
canvas.create_image(313, 209, image=img)
timer_text = canvas.create_text(315, 169, text="Timer", fill="#001C26", font=(FONT_NAME, 55, "bold"))
canvas.grid(column=0, row=1, columnspan=3)

#timer timings
#def start_timer():
   # reps = 

#timer count down mechanism
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)

def start_timer():
    count_down(65)  

#bottom panel
start = Button(text="Start", width=6, height=2, font=(FONT_NAME, 12, "bold"), command=start_timer)
start.grid(column=0, row=2, pady=5)

stop = Button(text="Reset", width=6, height=2, font=(FONT_NAME, 12, "bold"))
stop.grid(column=2, row=2, pady=5)

check_mark=Label(text="✓", width=6, height=2, fg="#00ff62")
check_mark.grid(column=1, row=2)

window.mainloop()