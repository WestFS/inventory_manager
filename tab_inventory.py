import customtkinter as ctk


class MainFrame:
    def __init__(self, frame_window):
        self.frame_window = frame_window
        self.frame_top = ctk.CTkFrame(master=frame_window, fg_color="#E0E0E0", width=1000, height=76, corner_radius=1)
        self.frame_top.pack(side="top", pady=5)
        self.frame_bottom = ctk.CTkFrame(master=frame_window, fg_color="#E0E0E0", width=1000, height=520)
        self.frame_bottom.pack(side="bottom")

        # Nesse parte do search eu preciso fazer uma QUERY de busca na lista de items para cada opção linkado ao entry
        label_search_option = ctk.CTkOptionMenu(self.frame_top, values=["Produto", "ID"],
                                                width=40, height=38, corner_radius=1)
        label_search_option.place(x=750, y=25)
        label_search_option.set("Search")

        label_entry_search = ctk.CTkEntry(master=self.frame_top, justify="left", corner_radius=1, height=38)
        label_entry_search.place(x=800, y=25)

        self.create_button_c = ctk.CTkButton(master=self.frame_top, text="CRIAR", command=MainFrame.open_new_window,
                                             width=100, height=38, corner_radius=3, fg_color="#00FA9A",
                                             text_color="Black")
        self.create_button_c.place(x=15, y=25)

        self.create_button_u = ctk.CTkButton(master=self.frame_top, text="ALTERAR", command=MainFrame.open_new_window,
                                             width=100, height=38, corner_radius=3, fg_color="#FFF0BD",
                                             text_color="Black")

        self.create_button_u.place(x=125, y=25)

    @staticmethod
    def open_new_window():
        new_window_product = ctk.CTk()
        new_window_product.title("NOVO PRODUTO")

        width = 500
        height = 250

        screen_width = new_window_product.winfo_screenwidth()
        screen_height = new_window_product.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        new_window_product.geometry('%dx%d+%d+%d' % (width, height, x, y))

        label = ctk.CTkLabel(master=new_window_product, text="Você está criando um novo item")
        label.pack()

        new_window_product.resizable(width=False, height=False)
        new_window_product.mainloop()
