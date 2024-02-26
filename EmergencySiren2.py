import winsound
import tkinter as tk
class AlertButton:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Program by Zidaan")
        self.root.geometry("400x300")
        self.root.bind("<Key>", self.keypress)
        self.message = tk.StringVar()
        self.message.set("(Program by Zidaan) \n Click the button if \n you are not feeling well \n and click 0 to stop ")
        self.label = tk.Label(self.root, textvariable=self.message, font=("Arial", 20), fg="white", bg="black")
        self.label.pack(pady=30)
        self.button = tk.Button(self.root, text="Help Me !!!", bg="red", fg="white", font=("Arial", 20), command=self.beep)
        self.button.pack(pady=30)
        self.root.mainloop()
    def beep(self):
        self.message.set("Help me please !!! \n My health is not well. \n I have fallen unconscious. \n Emergency !!!")
        while True:
            winsound.Beep(1000, 500)
            self.root.update()
            if self.message.get() == "Click the button if \n you are not feeling well":
                break            
    def keypress(self, event):
        if event.char == "0":
            self.message.set("Click the button if \n you are not feeling well")
AlertButton()
