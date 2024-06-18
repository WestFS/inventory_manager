import customtkinter as ctk
from tab_inventory import MainFrame


class MenuView(ctk.CTkTabview):
    def __init__(self, main_window, **kwargs):
        super().__init__(main_window, **kwargs)
        self.add("HOME")
        self.add("INVENTORY")
        self.add("SALES")


class Screen(ctk.CTk):
    def __init__(self):
        super().__init__()

        width = 1080
        height = 620

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.tab_view = MenuView(main_window=self)
        self.tab_view.configure(width=1080, height=620)
        self.tab_view.pack()
        self.tab_inv = self.tab_view.tab("INVENTORY")
        MainFrame(frame_window=self.tab_inv)


root = Screen()
root.title("IMS")
root.after(0, lambda: root.state())
root.mainloop()
