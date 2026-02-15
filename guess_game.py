import tkinter as tk
import random

# ------------------ تنظیمات اولیه ------------------
secret_number = random.randint(1, 100)
attempts = 0

# ------------------ توابع ------------------
def check_guess(event=None):   # ← event اضافه شد برای Enter
    global attempts
    attempts += 1

    try:
        guess = int(entry.get())

        if guess < secret_number:
            result_label.config(text="⬆ Bigger!", fg="#ff4da6")
        elif guess > secret_number:
            result_label.config(text="⬇ Smaller!", fg="#ff4da6")
        else:
            result_label.config(
                text=f"💖 You Win!\nTries: {attempts}",
                fg="#6a0dad"
            )
            guess_btn.config(state="disabled")

    except:
        result_label.config(text="Enter a valid number!", fg="red")


def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="Guess a number (1-100) 💜", fg="#5a189a")
    entry.delete(0, tk.END)
    guess_btn.config(state="normal")


# ------------------ پنجره اصلی ------------------
window = tk.Tk()
window.title("💗 Guess Game")
window.geometry("420x480")
window.resizable(False, False)
window.configure(bg="#f8c8dc")

# قاب بیرونی (استایل کارتونی)
outer_frame = tk.Frame(window, bg="#ff99cc", bd=6)
outer_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=400)

inner_frame = tk.Frame(outer_frame, bg="#ffe6f2")
inner_frame.pack(expand=True, fill="both", padx=8, pady=8)

# عنوان
title = tk.Label(
    inner_frame,
    text="💜 Guess The Number 💜",
    font=("Comic Sans MS", 16, "bold"),
    bg="#ffe6f2",
    fg="#7b2cbf"
)
title.pack(pady=15)

# متن نتیجه
result_label = tk.Label(
    inner_frame,
    text="Guess a number (1-100) 💕",
    font=("Comic Sans MS", 11),
    bg="#ffe6f2",
    fg="#5a189a"
)
result_label.pack(pady=10)

# ورودی
entry = tk.Entry(
    inner_frame,
    font=("Comic Sans MS", 14),
    justify="center",
    bd=2,
    width=15
)
entry.pack(pady=15, ipady=5)

entry.focus()

# وقتی Enter بزنیم اجرا بشه
window.bind("<Return>", check_guess)

# دکمه حدس
guess_btn = tk.Button(
    inner_frame,
    text="💗 Guess 💗",
    font=("Comic Sans MS", 12, "bold"),
    bg="#ff66b2",
    fg="white",
    activebackground="#ff3385",
    width=18,
    height=2,
    bd=0,
    command=check_guess
)
guess_btn.pack(pady=8)

# دکمه ریست
reset_btn = tk.Button(
    inner_frame,
    text="🔄 Reset",
    font=("Comic Sans MS", 11, "bold"),
    bg="#c77dff",
    fg="white",
    activebackground="#9d4edd",
    width=18,
    height=2,
    bd=0,
    command=reset_game
)
reset_btn.pack(pady=8)

window.mainloop()
