import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        master.title("Python Link Generator v.01")
        master.geometry("425x175")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = tk.Button(self)
        self.button1["text"] = "Button1"
        self.button1["command"] = self.button1_output
        #self.button1.pack(side="top")

        self.quit = tk.Button(self, text="Quit", fg="red",
                                command=self.master.destroy)
        #self.quit.pack(side="bottom")

    def button1_output(self):
        pass

        
root = tk.Tk()
app = Application(master=root)
app.mainloop()
