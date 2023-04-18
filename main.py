from tkinter import *
import math
checkmark = "🗸"
timer = None
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 1


# ---------------------------- TIMER RESET ------------------------------- #
def cancel_timer():
    global rep, checkmark
    window.after_cancel(timer)
    text.config(text="Timer")
    text1.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    rep = 1
    checkmark = "🗸"


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep, checkmark
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep == 1 or rep == 3 or rep == 5 or rep == 7:
        count_timer(work_sec)
        text.config(text="Work Time", fg=YELLOW)
        text1.config(text=checkmark)
        checkmark += "🗸"
    elif rep == 2 or rep == 4 or rep == 6:
        count_timer(short_break_sec)
        text.config(text="Break Time", fg=PINK)
    else:
        count_timer(long_break_sec)
        text.config(text="Break Time", fg=RED)
    if rep < 8:
        rep += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_timer(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_timer, count-1)
    else:
        start_timer()


# ---------------------------- GUI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=150, pady=100, bg=GREEN)

text = Label(text="TIMER", font=(FONT_NAME, 35, "bold"), fg=RED, bg=GREEN)
text.grid(row=0, column=1)

text1 = Label(font=(FONT_NAME, 20, "bold"), fg=RED, bg=GREEN)
text1.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2,  column=0)
stop_button = Button(text="reset", command=cancel_timer)
stop_button.grid(row=2,  column=2)

window.mainloop()
