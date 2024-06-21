from tkinter import CENTER, ttk
import customtkinter as ctk
from datetime import date
from tkinter import messagebox


class ChangeLog:
    def __init__(self):
        self.log_entries = []

    def add_entry(self, entry):
        self.log_entries.append(entry)

        # Aqui você pode salvar em um arquivo, banco de dados, etc.
        print("Log Entry:", entry)


class MainFrame:
    def __init__(self, frame_window):
        self.frame_window = frame_window
        self.quantity_product = None
        self.value_unity_product = None
        self.label_total_cost = None
        self.total_cost_var = None
        self.date_entry_calendar = None
        self.tree_table = None
        self.info_window_product = None
        self.quantity_entry = None
        self.price_entry = None
        self.lista = []

        self.id_counter = 1

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

        self.create_button_u = ctk.CTkButton(master=self.frame_top, text="ALTERAR", command=self.show_info_product,
                                             width=100, height=38, corner_radius=3, fg_color="#FFF0BD",
                                             text_color="Black")
        self.create_button_u.place(x=125, y=25)

        # Chamada para configurar o TreeView na aba INVENTORY
        self.setup_tree_view()

    def setup_tree_view(self):
        # Exemplo de dados para a lista
        self.lista = []

        # Cabeçalho da tabela
        table_header = ["ID", "Nome do Produto", "Categoria", "Quantidade", "Preço Unitário", "Preço Total", "Data"]

        # TreeView
        self.tree_table = ttk.Treeview(master=self.frame_bottom, columns=table_header, show="headings")

        # Scrollbars
        tree_vsb = ttk.Scrollbar(master=self.frame_bottom, orient="vertical", command=self.tree_table.yview)
        tree_hsb = ttk.Scrollbar(master=self.frame_bottom, orient="horizontal", command=self.tree_table.xview)
        self.tree_table.configure(yscrollcommand=tree_vsb.set, xscrollcommand=tree_hsb.set)
        self.tree_table.grid(row=0, column=0, sticky="nsew")
        self.tree_table.config(height=500)

        # configurações de estilo da tabela
        self.tree_table.tag_configure("my_font", font=("Helvetica", 12))
        self.tree_table.tag_configure("my_bg", background="#D9E2DE")

        tree_vsb.grid(row=0, column=1, sticky="ns")
        tree_hsb.grid(row=1, column=0, sticky="ew")

        self.frame_bottom.grid_rowconfigure(0, weight=1)
        self.frame_bottom.grid_columnconfigure(0, weight=1)

        # Configuração das colunas
        header = ["nw", "nw", "nw", "nw", "ne", "ne", "center"]
        column_width = [50, 275, 180, 110, 130, 130, 110]

        i = 0

        for i, col in enumerate(table_header):
            self.tree_table.heading(col, text=col.title(), anchor=CENTER)
            # Ajusta as colunas de acordo com o os titulo da lista
            self.tree_table.column(col, width=column_width[i], anchor=header[i])

        i += 1

        for i, item in enumerate(self.lista):
            tags = ("my_font", "my_bg" if i % 2 == 0 else "")
            self.tree_table.insert("", "end", values=item, tags=tags)

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
                                      placeholder_text="Nome do produto...", width=100, validate="key",
                                      validatecommand=[new_window_product.register
                                                       (self.validate_not_number_input), '%S'])

        create_product.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        label_category = ctk.CTkLabel(master=new_window_product, text="Categoria: ", font=('Ivy', 12, "bold"))
        label_category.grid(row=1, column=2, pady=5, sticky="e")
        category_product = ctk.CTkEntry(master=new_window_product, width=100, validate="key",
                                        validatecommand=[new_window_product.register
                                                         (self.validate_not_number_input), '%S'])

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
                                                                 '%P'))
        self.value_unity_product.insert(0, 'R$ ')
        self.value_unity_product.grid(row=2, column=3, pady=5, sticky="ew")

        self.label_total_cost = ctk.CTkLabel(master=new_window_product, text='Total: R$ 0,00',
                                             font=('Ivy', 12, "bold")
                                             )
        self.label_total_cost.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        button_update = ctk.CTkButton(master=new_window_product, text="Calcular", command=self.calculate_total,
                                      width=10)
        button_update.place(x=150, y=128)

        finish_create_product = ctk.CTkButton(master=new_window_product, text="Finalizar Cadastro",
                                              command=lambda: self.finalizar_cadastro(create_product, category_product),
                                              width=15)
        finish_create_product.place(x=225, y=180)

        new_window_product.resizable(width=False, height=False)
        new_window_product.mainloop()

    def finalizar_cadastro(self, create_product_entry, category_product_entry):
        # Método para finalizar o cadastro do produto
        nome_produto = create_product_entry.get()
        categoria = category_product_entry.get()
        quantidade = self.quantity_product.get()
        valor_unitario = self.value_unity_product.get()

        # Validação simples para garantir que todos os campos foram preenchidos
        if nome_produto and categoria and quantidade and valor_unitario:
            # Converte quantidade e valor unitário para os tipos  int e float
            quantidade = int(quantidade)
            valor_unitario = float(valor_unitario.replace('R$ ', '').replace(',', '.'))

            # Captura a data atual
            data_atual = date.today().strftime('%Y-%m-%d')

            # Adiciona os dados à lista com um ID autoincrementável
            novo_produto = [self.id_counter, nome_produto, categoria, quantidade, valor_unitario,
                            quantidade * valor_unitario, data_atual]
            self.lista.append(novo_produto)

            # Incrementa o contador de ID para o próximo produto
            self.id_counter += 1

            # Atualiza a exibição na TreeView
            self.update_tree_view()

            # Fecha a janela de cadastro
            create_product_entry.delete(0, 'end')
            category_product_entry.delete(0, 'end')
            self.quantity_product.delete(0, 'end')
            self.value_unity_product.delete(0, 'end')

    def update_tree_view(self):
        # Limpa a TreeView atual
        for item in self.tree_table.get_children():
            self.tree_table.delete(item)

        # Reinsere os dados atualizados
        for i, item in enumerate(self.lista):
            tags = ("my_font", "my_bg" if i % 2 == 0 else "")
            self.tree_table.insert("", "end", values=item, tags=tags)

    @staticmethod
    def validate_number_input(char):
        # Esta função é chamada pelo validatecommand para validar se o caractere digitado é um número
        return char.isdigit()

    @staticmethod
    def validate_not_number_input(char):
        # Esta função é chamada pelo validatecommand para não deixar ser digitado um numero
        return not char.isdigit()

    @staticmethod
    def validate_real_input(new_value):
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

    def show_info_product(self):
        selected_item = self.tree_table.focus()
        if selected_item:
            item_data = self.tree_table.item(selected_item, 'values')

            # Cria uma nova janela para exibir as informações detalhadas
            self.info_window_product = ctk.CTkToplevel()
            self.info_window_product.title("DETALHES DO PRODUTO")

            self.setup_product_details_window(item_data)

    def setup_product_details_window(self, item_data):
        # Configuração da janela de detalhes do produto
        self.info_window_product.grid_columnconfigure(0, weight=1)
        self.info_window_product.grid_columnconfigure(1, weight=1)

        id_product_label = ctk.CTkLabel(master=self.info_window_product, text=f"ID: {item_data[0]}",
                                        font=('Ivy', 12, "bold"))
        id_product_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        name_product_label = ctk.CTkLabel(master=self.info_window_product, text=f"Nome do Produto: {item_data[1]}",
                                          font=('Ivy', 12, "bold"))
        name_product_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

        label_category = ctk.CTkLabel(master=self.info_window_product, text=f"Categoria: {item_data[2]}",
                                      font=('Ivy', 12, "bold"))
        label_category.grid(row=2, column=0, padx=10, pady=5, sticky='w')

        label_quantity = ctk.CTkLabel(master=self.info_window_product, text=f"Quantidade:",
                                      font=('Ivy', 12, "bold"))
        label_quantity.grid(row=3, column=0, padx=10, pady=5, sticky='w')

        self.quantity_entry = ctk.CTkEntry(master=self.info_window_product, width=100)
        self.quantity_entry.insert(0, str(item_data[3]))  # Insere valor atual
        self.quantity_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        try:
            price_per_unit = float(item_data[4])
            label_cost_unit = ctk.CTkLabel(master=self.info_window_product,
                                           text=f"Preço Unitário:",
                                           font=('Ivy', 12, "bold"))
            label_cost_unit.grid(row=4, column=0, padx=10, pady=5, sticky='w')

            self.price_entry = ctk.CTkEntry(master=self.info_window_product, width=100)
            self.price_entry.insert(0, f"R$ {price_per_unit:.2f}")  # Insere valor atual
            self.price_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        except ValueError:
            label_cost_unit = ctk.CTkLabel(master=self.info_window_product, text=f"Preço Unitário: {item_data[4]}",
                                           font=('Ivy', 12, "bold"))
            label_cost_unit.grid(row=4, column=0, padx=10, pady=5, sticky='w')

        try:
            total_cost = float(item_data[5])
            label_cost_total = ctk.CTkLabel(master=self.info_window_product,
                                            text=f"Preço Total: R$ {total_cost:.2f}",
                                            font=('Ivy', 12, "bold"))
            label_cost_total.grid(row=5, column=0, padx=10, pady=5, sticky='w')

        except ValueError:
            label_cost_total = ctk.CTkLabel(master=self.info_window_product, text=f"Preço Total: {item_data[5]}",
                                            font=('Ivy', 12, "bold"))
            label_cost_total.grid(row=5, column=0, padx=10, pady=5, sticky='w')

        label_date = ctk.CTkLabel(master=self.info_window_product, text=f"Data: {item_data[6]}",
                                  font=('Ivy', 12, "bold"))
        label_date.grid(row=6, column=0, padx=10, pady=5, sticky='w')

        btn_conclude = ctk.CTkButton(master=self.info_window_product, text="Concluir Alteração",
                                     command=self.conclude_changes)
        btn_conclude.grid(row=7, column=0, padx=10, pady=10, sticky='w')

        btn_delete = ctk.CTkButton(master=self.info_window_product, text="Deletar Item", command=self.delete_item)
        btn_delete.grid(row=7, column=1, padx=10, pady=10, sticky='e')

        self.info_window_product.resizable(width=False, height=False)

    def conclude_changes(self):
        selected_item = self.tree_table.focus()
        if selected_item:
            item_data = self.tree_table.item(selected_item, 'values')

            new_quantity = self.quantity_entry.get()
            new_price_str = self.price_entry.get()

            try:
                new_quantity = int(new_quantity)
                new_price = float(
                    new_price_str.lstrip('R$ ').replace(',', '.'))  # Limpar formatação e converter para float
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")
                return

            # Registro da alteração no log
            log_entry = {
                'ID': item_data[0],
                'Nome do Produto': item_data[1],
                'Categoria': item_data[2],
                'Quantidade Antes': item_data[3],
                'Preço Unitário Antes': item_data[4],
                'Preço Total Antes': item_data[5],
                'Data': item_data[6],
                'Ação': 'Alteração',
                'Quantidade Nova': new_quantity,
                'Preço Unitário Novo': new_price,
                'Preço Total Novo': new_quantity * new_price
            }
            print(log_entry)

            # Atualiza os valores na Treeview
            item_data_updated = list(item_data)
            item_data_updated[3] = new_quantity
            item_data_updated[4] = new_price
            item_data_updated[5] = new_quantity * new_price
            self.tree_table.item(selected_item, values=tuple(item_data_updated))

            # Atualiza os campos na janela de detalhes do produto
            self.quantity_entry.delete(0, 'end')
            self.quantity_entry.insert(0, str(new_quantity))
            self.price_entry.delete(0, 'end')
            self.price_entry.insert(0, f"R$ {new_price:.2f}")

    def delete_item(self):
        selected_item = self.tree_table.focus()
        if selected_item:
            item_data = self.tree_table.item(selected_item, 'values')

            confirm_delete = messagebox.askyesno(title="Confirmar Exclusão",
                                                 message="Tem certeza que deseja excluir este item?")
            if confirm_delete:
                # Registro da exclusão no log
                log_entry = {
                    'ID': item_data[0],
                    'Nome do Produto': item_data[1],
                    'Categoria': item_data[2],
                    'Quantidade': item_data[3],
                    'Preço Unitário': item_data[4],
                    'Preço Total': item_data[5],
                    'Data': item_data[6],
                    'Ação': 'Exclusão'
                }
                print(log_entry)  # Salvar em um arquivo ou banco de dados

                # Implemente a lógica para deletar o item da Treeview e possivelmente do banco de dados
                self.tree_table.delete(selected_item)

                if self.info_window_product:
                    self.info_window_product.destroy()
