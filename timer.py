from tkinter import *
import math
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "#FF5D58"
YELLOW = "#021526"
FONT_NAME = "Courier"
WORK_MIN = 2
FOUCS_ON_YOUR_WORK = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
     window.after_cancel(timer)
     #timer_text 00:00
     Canvas.itemconfig(timer_text, text="00:00")
     #title_lable "Timer"
     title_label.config(text="Timer")
     #reset check_mark
     check_mark.config(text="")
     global reps
     reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
   global reps
   reps += 1

   break_sec =WORK_MIN * 60
   work_sec = FOUCS_ON_YOUR_WORK * 60

   if reps % 2 == 0:
        count_down(work_sec)
        title_label.config(text="Foucs On Your Work")
   else:
        count_down(break_sec)
        title_label.config(text="Take A Break And Relex")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
       count_sec = f"0{count_sec}"

    Canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
     global timer
     timer = window.after(1000, count_down, count - 1)
    else:
     start_timer()
     marks = ""
     work_sessions = math.floor(reps/2)
     for _ in range(work_sessions):
          marks += "✔"
          check_mark.config(text=marks)
     # Timer has reached 0, play a beep sound
     winsound.Beep(5000, 5000)  # Frequency 1000 Hz, duration 1000 ms (1 second)
        # You can also add additional functionality here (like a message or changing the state)
     Canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer")
window.config(padx=50, pady=10, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(row=0, column=1)

owner_label = Label(text="© 2025 MultiQoS Technologies - All rights reserved.", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
owner_label.grid(row=4, column=1)

created_by_label = Label(text="Created by Kushal", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
created_by_label.grid(row=5, column=1)

Canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="F:/Kushal/Programing/Python Programing/Application/pamdora app/tomato.png")
Canvas.create_image(100, 112, image=tomato_img)
timer_text =Canvas.create_text(100, 25, text="00:00", fill="white", font=("Roboto Mono", 45, "bold"))
Canvas.grid(column=1, row=1)


start_button = Button(
    text="Start", 
    width=10, 
    command=start_timer, 
    bg=GREEN,      # Button background color
    fg="white",     # Button text color
    font=(FONT_NAME, 15, "bold"),  # Font style and size
    relief="solid",  # Border around button
    borderwidth=3,   # Border thickness
    padx=5,         # Horizontal padding
    pady=5,          # Vertical padding
    activebackground=GREEN,  # Background color when button is clicked
    activeforeground=GREEN     # Text color when button is clicked
)
start_button.grid(row=2, column=0)

restart_button = Button(
    text="Restart", 
    width=10, 
    command=reset_timer, 
    bg=GREEN, 
    fg="white", 
    font=(FONT_NAME, 15, "bold"), 
    relief="solid", 
    borderwidth=3, 
    padx=5, 
    pady=5, 
    activebackground=GREEN, 
    activeforeground=GREEN
)
restart_button.grid(row=2, column=2, )

check_mark = Label(fg="#16C47F", bg=YELLOW, font=(FONT_NAME, 25))
check_mark.grid(row=3, column=1)

window.mainloop()