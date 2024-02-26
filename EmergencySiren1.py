import tkinter as tk
import threading
import winsound
class BeepButtonApp:
    def __init__(self, master):
        self.master = master
        master.title(" Program by Zidaan")
        self.beep_button = tk.Button(master, text="Help Me !!!", fg="white", bg="red", font=(
            "Arial", 24), command=self.start_beeping)
        self.beep_button.pack(fill=tk.BOTH, expand=True)
        self.stop_button = tk.Button(master, text="Iam Okay !!!", fg="white", bg="green", font=(
            "Arial", 24), command=self.stop_beeping)
        self.stop_button.pack(fill=tk.BOTH, expand=True)
        self.message_label = tk.Label(
            master, text="", fg="white", bg="black", font=("Arial", 40))
        self.message_label.pack(fill=tk.BOTH, expand=True)
    def start_beeping(self):
        self.stop_pressed = False
        self.beep_thread = threading.Thread(target=self.continuous_beep)
        self.beep_thread.start()
        self.message_label.configure(
            text="Help me !!! \n My health is not well. \n I have fallen unconscious.")
    def stop_beeping(self):
        self.stop_pressed = True
        self.message_label.configure(text="I am okay,\n Nothing to worry")
    def continuous_beep(self):
        while not self.stop_pressed:
            winsound.Beep(1000, 1000)
    def exit(self):
        self.stop_pressed = True
        self.beep_thread.join()
        self.master.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    app = BeepButtonApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit)
    root.mainloop()
