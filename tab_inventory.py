import customtkinter as ctk


class MainFrame:
    def __init__(self, frame_window):
        self.frame_window = frame_window
        self.quantity_product = None
        self.value_unity_product = None
        self.label_total_cost = None

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

        self.create_button_c = ctk.CTkButton(master=self.frame_top, text="CRIAR", command=self.open_new_window,
                                             width=100, height=38, corner_radius=3, fg_color="#00FA9A",
                                             text_color="Black")
        self.create_button_c.place(x=15, y=25)

        self.create_button_u = ctk.CTkButton(master=self.frame_top, text="ALTERAR", command=self.open_new_window,
                                             width=100, height=38, corner_radius=3, fg_color="#FFF0BD",
                                             text_color="Black")
        self.create_button_u.place(x=125, y=25)

    def open_new_window(self):
        new_window_product = ctk.CTk()
        new_window_product.title("NOVO PRODUTO")

        width = 520
        height = 250

        screen_width = new_window_product.winfo_screenwidth()
        screen_height = new_window_product.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        new_window_product.geometry('%dx%d+%d+%d' % (width, height, x, y))

        label_title_c = ctk.CTkLabel(master=new_window_product, text="AREA DE CADASTRO DE NOVO PRODUTO")
        label_title_c.grid(row=0, column=0, pady=10, columnspan=4, sticky="nsew")

        label_product = ctk.CTkLabel(master=new_window_product, text="Nome do Produto: ", font=("Arial", 12))
        label_product.grid(row=1, column=0, pady=5, sticky="e")
        create_product = ctk.CTkEntry(master=new_window_product,
                                      placeholder_text="Nome do produto...", width=100)
        create_product.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        label_category = ctk.CTkLabel(master=new_window_product, text="Categoria: ", font=("Arial", 12))
        label_category.grid(row=1, column=2, pady=5, sticky="e")
        category_product = ctk.CTkEntry(master=new_window_product, width=100)
        category_product.grid(row=1, column=3, pady=5, sticky="ew")

        label_quantity = ctk.CTkLabel(master=new_window_product, text="Quantidade de Produto: ", font=("Arial", 12))
        label_quantity.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.quantity_product = ctk.CTkEntry(master=new_window_product, validate="key",
                                             validatecommand=(new_window_product.register(self.validate_number_input),
                                                              '%S'))
        self.quantity_product.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        label_value_unity = ctk.CTkLabel(master=new_window_product, text="Valor unitario: ", font=("Arial", 12))
        label_value_unity.grid(row=2, column=2, pady=5, sticky="e")

        self.value_unity_product = ctk.CTkEntry(master=new_window_product, validate="key",
                                                validatecommand=(new_window_product.register(self.validate_real_input),
                                                                 '%P', '%V'))
        self.value_unity_product.insert(0, 'R$ ')
        self.value_unity_product.grid(row=2, column=3, pady=5, sticky="ew")

        self.label_total_cost = ctk.CTkLabel(master=new_window_product, text='Total: R$ 0,00')
        self.label_total_cost.grid(row=3, column=0, pady=5, sticky="e")

        button_update = ctk.CTkButton(master=new_window_product, text="Calcular", command=self.calculate_total)
        button_update.grid(row=3, column=1, pady=5, sticky="ew")

        new_window_product.resizable(width=False, height=False)
        new_window_product.mainloop()

    @staticmethod
    def validate_number_input(char):
        # Esta função é chamada pelo validatecommand para validar se o caractere digitado é um número
        return char.isdigit()

    @staticmethod
    def validate_real_input(entry_value, new_value):
        # Permite dígitos, uma única vírgula ou ponto e o símbolo 'R$' no início
        if (new_value.isdigit() or (new_value.count(',') < 2) or (new_value.count('.') < 2)
                or new_value.startswith('R$ ')):
            return True
        return False

    def calculate_total(self):
        # Obtém os valores dos campos de entrada
        quantity_str = self.quantity_product.get()
        value_str = self.value_unity_product.get()

        # Remove 'R$ ' e substitui ',' por '.' para garantir que o valor possa ser convertido para float
        value_str = value_str.replace('R$ ', '').replace(',', '.')

        try:
            # Converte os valores para float e calcula o total
            quantity = float(quantity_str)
            value_per_unit = float(value_str)
            total_cost = quantity * value_per_unit

            # Atualiza o label com o total formatado
            self.label_total_cost['text'] = f'Total: R$ {total_cost:.2f}'
        except ValueError:
            # Em caso de erro na conversão para float
            self.label_total_cost['text'] = 'Total: R$ 0,00'
