import tkinter as tk
import time
import random
root = tk.Tk()
root.title("Colour Changing Digital Clock")
root.geometry("355x235")
root.configure(bg="black")
message_label = tk.Label(root, font=("Arial", 20), fg="white", bg="black", text="Digital Colour Changing \n Clock by Zidaan")
message_label.pack()
clock_label = tk.Label(root, font=("Arial", 35), fg="white", bg="black")
clock_label.pack(pady=20)
date_label = tk.Label(root, font=("Arial", 20), fg="white", bg="black")
date_label.pack(pady=20)
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    current_date = time.strftime("%A, %B %d, %Y")
    date_label.config(text=current_date)
    clock_label.config(fg=get_random_color())
    message_label.config(fg=get_random_color())
    date_label.config(fg=get_random_color())
    root.after(1000, update_time)
def get_random_color():
    r = lambda: hex(random.randint(0, 255))[2:].zfill(2)
    return "#" + r() + r() + r()
update_time()
root.mainloop()
