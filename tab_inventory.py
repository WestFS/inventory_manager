from tkinter import CENTER, ttk
import customtkinter as ctk
from tkcalendar import DateEntry


class MainFrame:
    def __init__(self, frame_window):
        self.frame_window = frame_window
        self.quantity_product = None
        self.value_unity_product = None
        self.label_total_cost = None
        self.total_cost_var = None
        self.date_entry_calendar = None

        self.frame_top = ctk.CTkFrame(master=frame_window, fg_color="#E0E0E0", width=1000, height=76, corner_radius=1)
        self.frame_top.grid(row=0, column=0, padx=25)
        self.frame_bottom = ctk.CTkFrame(master=frame_window, fg_color="#E0E0E0", width=1000, height=520)
        self.frame_bottom.grid(row=1, column=0, padx=10, pady=5)

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

        # Chamada para configurar o TreeView na aba INVENTORY
        self.setup_tree_view()

    def setup_tree_view(self):
        # Exemplo de dados para a lista
        lista = [
            [1, 'Produto A', 'Categoria A', 10, 15.99, 159.90, '2024-06-19'],
            [2, 'Produto B', 'Categoria B', 5, 29.99, 149.95, '2024-06-19']
        ]

        # Cabeçalho da tabela
        table_header = ["ID", "Nome do Produto", "Categoria", "Quantidade", "Preço Unitário", "Preço Total", "Data"]

        # TreeView
        tree_table = ttk.Treeview(master=self.frame_bottom, columns=table_header, show="headings")

        # Scrollbars
        tree_vsb = ttk.Scrollbar(master=self.frame_bottom, orient="vertical", command=tree_table.yview)
        tree_hsb = ttk.Scrollbar(master=self.frame_bottom, orient="horizontal", command=tree_table.xview)
        tree_table.configure(yscrollcommand=tree_vsb.set, xscrollcommand=tree_hsb.set)
        tree_table.grid(row=0, column=0, sticky="nsew")
        tree_table.config(height=500)

        # configurações de estilo da tabela
        tree_table.tag_configure("my_font", font=("Helvetica", 12))
        tree_table.tag_configure("my_bg", background="#D9E2DE")

        tree_vsb.grid(row=0, column=1, sticky="ns")
        tree_hsb.grid(row=1, column=0, sticky="ew")

        self.frame_bottom.grid_rowconfigure(0, weight=1)
        self.frame_bottom.grid_columnconfigure(0, weight=1)

        # Configuração das colunas
        header = ["nw", "nw", "nw", "nw", "ne", "ne", "center"]
        column_width = [50, 275, 180, 110, 130, 130, 110]

        i = 0

        for i, col in enumerate(table_header):
            tree_table.heading(col, text=col.title(), anchor=CENTER)
            # Ajusta as colunas de acordo com o os titulo da lista
            tree_table.column(col, width=column_width[i], anchor=header[i])

        i += 1

        for i, item in enumerate(lista):
            tags = ("my_font", "my_bg" if i % 2 == 0 else "")
            tree_table.insert("", "end", values=item, tags=tags)

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

        label_title_c = ctk.CTkLabel(master=new_window_product, text="AREA DE CADASTRO DE NOVO PRODUTO",
                                     font=('Ivy', 15, "bold"))
        label_title_c.grid(row=0, column=0, pady=10, columnspan=4, sticky="nsew")

        label_product = ctk.CTkLabel(master=new_window_product, text="Nome do Produto: ", font=('Ivy', 12, "bold"))
        label_product.grid(row=1, column=0, pady=5, sticky="e")
        create_product = ctk.CTkEntry(master=new_window_product,
                                      placeholder_text="Nome do produto...", width=100)
        create_product.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        label_category = ctk.CTkLabel(master=new_window_product, text="Categoria: ", font=('Ivy', 12, "bold"))
        label_category.grid(row=1, column=2, pady=5, sticky="e")
        category_product = ctk.CTkEntry(master=new_window_product, width=100)
        category_product.grid(row=1, column=3, pady=5, sticky="ew")

        label_quantity = ctk.CTkLabel(master=new_window_product, text="Quantidade de Produto: ",
                                      font=('Ivy', 12, "bold"))
        label_quantity.grid(row=2, column=0, padx=2, pady=5, sticky="e")
        self.quantity_product = ctk.CTkEntry(master=new_window_product, validate="key",
                                             validatecommand=(new_window_product.register
                                                              (self.validate_number_input), '%S'))
        self.quantity_product.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        label_value_unity = ctk.CTkLabel(master=new_window_product, text="Valor unitario: ", font=('Ivy', 12, "bold"))
        label_value_unity.grid(row=2, column=2, pady=2, sticky="e")

        self.value_unity_product = ctk.CTkEntry(master=new_window_product, validate="key",
                                                validatecommand=(new_window_product.register(self.validate_real_input),
                                                                 '%P', '%V'))
        self.value_unity_product.insert(0, 'R$ ')
        self.value_unity_product.grid(row=2, column=3, pady=5, sticky="ew")

        self.label_total_cost = ctk.CTkLabel(master=new_window_product, text='Total: R$ 0,00',
                                             font=('Ivy', 12, "bold")
                                             )
        self.label_total_cost.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        button_update = ctk.CTkButton(master=new_window_product, text="Calcular", command=self.calculate_total,
                                      width=10)
        button_update.place(x=150, y=125)

        label_calendar = ctk.CTkLabel(master=new_window_product, text="DATA:", font=('Ivy', 12, "bold"))
        label_calendar.place(x=250, y=125)
        self.date_entry_calendar = DateEntry(master=new_window_product, background="darkblue", foreground="white",
                                             borderwidth=4, locale="pt_BR", date_pattern="dd-mm-yyyy")
        self.date_entry_calendar.place(x=290, y=127)

        finish_create_product = ctk.CTkButton(master=new_window_product, text="Finalizar Cadastro",
                                              command=lambda: self.finalizar_cadastro(create_product, category_product),
                                              width=15)
        finish_create_product.place(x=250, y=180)

        new_window_product.resizable(width=False, height=False)
        new_window_product.mainloop()

    def finalizar_cadastro(self, create_product_entry, category_product_entry):
        # Método para finalizar o cadastro do produto
        nome_produto = create_product_entry.get()
        categoria = category_product_entry.get()
        quantidade = self.quantity_product.get()
        valor_unitario = self.value_unity_product.get()
        data_de_criacao = self.date_entry_calendar.get()

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
        try:
            # Obtém os valores dos campos de entrada
            quantity_str = self.quantity_product.get()
            value_str = self.value_unity_product.get()

            # Remove 'R$ ' e substitui ',' por '.' para garantir que o valor possa ser convertido para float
            value_str = value_str.replace('R$ ', '').replace(',', '.')

            # Converte os valores para float e calcula o total
            quantity = float(quantity_str)
            value_per_unit = float(value_str)
            total_cost = quantity * value_per_unit

            # Atualiza o label com o total formatado
            self.label_total_cost.configure(text=f'Total: R$ {total_cost:.2f}')

            # Adicione um print para verificar o resultado
            print(f"Quantidade: {quantity}, Valor unitário: {value_per_unit}, Total: {total_cost:.2f}")
        except ValueError:
            # Em caso de erro na conversão para float
            self.total_cost_var.set('Total: R$ 0,00')

