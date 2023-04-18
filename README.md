<h1>Pomodoro Timer using Python Tkinter</h1>

![Screenshot (12)](https://user-images.githubusercontent.com/87391223/232821175-40cdede7-86c2-4ad9-b097-ca4644a32fb3.png)

This is a simple Pomodoro timer application built using Python Tkinter GUI toolkit. It can help you manage your time and increase productivity by using the Pomodoro technique.
Requirements

    Python 3.x
    tkinter module (usually included in Python standard library)

<h2>Installation</h2>

    Clone this repository to your local machine or download the source code as a zip file.
    Run the main.py script to start the timer.

## Functions:
TIMER RESET:
```python
def cancel_timer():
    global rep, checkmark
    window.after_cancel(timer)
    text.config(text="Timer")
    text1.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    rep = 1
    checkmark = "🗸"
```
TIMER MECHANISM:
```python
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
        rep += 1"
```
COUNTDOWN MECHANISM:
```python
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
    checkmark = "🗸"
```
<h2>Usage</h2>
The Pomodoro Timer is a simple, user-friendly application with a straightforward interface. Here are the steps to use the timer:

    Launch the application by running main.py.
    Select the duration of the timer using the drop-down menus for work and break sessions.
    Click the Start button to begin the timer.
    When the timer is running, the application displays the time remaining in the current session.
    Once the session is complete, the timer automatically switches to the next session (work or break) until the desired number of sessions is completed.
    To reset the timer, click the Reset button.

That's it! With this Pomodoro Timer, you can easily manage your time and increase productivity using the Pomodoro technique.
 ## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
## Find me on
[![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0D76A8)](https://www.linkedin.com/in/gokul-bakkiyarasu-531535251)
