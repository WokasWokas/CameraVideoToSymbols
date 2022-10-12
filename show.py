from font import FontSize
from tkinter import (
    Tk, 
    Label, 
    CENTER,
)

class App(Tk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def start(self) -> None:
        self.mainloop()

class ImageApp(App):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fontsize = FontSize(1)
        self.geometry("1280x720")

        self.bind("<Button-5>", self.up_size)
        self.bind("<Button-4>", self.down_size)

        self.label = Label(self)
        self.label.configure(
            justify=CENTER,
            width=1280, height=720,
            padx=10, pady=10,
            font=("Arial", self.fontsize.size),
            bg="#000000", fg="#FFFFFF",
        )
        self.label.pack()

    def loop_func(self, func, *args, **kwargs) -> None:
        try:
            func(*args, **kwargs)
            self.after(20, self.loop_func, func, *args, **kwargs)
        except Exception as error:
            print(error)
            return
    
    def update_label(self, data: str) -> None:
        self.label.configure(text=data)

    def up_size(self, event) -> None:
        self.fontsize.up_size()
        self.label.configure(font=("Arial", self.fontsize.size))
        self.label.pack()

    def down_size(self, event) -> None:
        self.fontsize.down_size()
        self.label.configure(font=("Arial", self.fontsize.size))
        self.label.pack()
    
    def set_label_resolution(self, nres: tuple[int ,int]) -> None:
        self.label.configure(
            width=nres[0] , height=nres[1]
        )
