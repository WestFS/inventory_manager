import customtkinter as ctk
from tkinter import ttk
from db_postgres.connection_db import connect_to_db


class LogFrame:
    def __init__(self, frame_window):
        self.frame_window = frame_window
        self.btn_export = None
        self.btn_search_all = None
        self.label_search_option = None
        self.label_btn_search = None
        self.label_entry_search = None
        self.lista = []
        self.frame_top = None
        self.frame_bottom = None
        self.tree_table = None  # Variável para o Treeview
        self.result_font = ctk.CTkFont(family="Arial", size=12)
        self.conn = connect_to_db()
        self.cursor = self.conn.cursor()

        # Configuração dos frames e widgets
        self.setup_ui()

        # Exibir todos os itens inicialmente
        self.show_all_items()


    def setup_ui(self):
        self.setup_frames()
        self.setup_search_widgets()
        self.setup_action_buttons()
        self.setup_tree_view()

    def setup_frames(self):
        self.frame_top = ctk.CTkFrame(master=self.frame_window, fg_color="#E0E0E0",
                                      width=1000, height=76, corner_radius=1)
        self.frame_top.grid(row=0, column=0, padx=25)

        self.frame_bottom = ctk.CTkFrame(master=self.frame_window, fg_color="#E0E0E0", width=1000, height=520)
        self.frame_bottom.grid(row=1, column=0, padx=10, pady=5)

    def setup_search_widgets(self):
        self.label_search_option = ctk.CTkOptionMenu(self.frame_top, values=["Produto", "ID", "Data"],
                                                     width=30, height=38, corner_radius=1)
        self.label_search_option.place(x=250, y=25)
        self.label_search_option.set("Opções")

        self.label_entry_search = ctk.CTkEntry(master=self.frame_top, justify="left",
                                               corner_radius=1, width=250, height=38)
        self.label_entry_search.place(x=300, y=25)

    def setup_action_buttons(self):
        self.label_btn_search = ctk.CTkButton(master=self.frame_top, text="Pesquisar",
                                              corner_radius=1, width=38, height=38,
                                              command=self.search_or_export)
        self.label_btn_search.place(x=500, y=25)

        self.btn_export = ctk.CTkButton(self.frame_top, text="Exportar", corner_radius=1, width=38, height=38,
                                        command=self.export_logs)
        self.btn_export.place(x=650, y=25)

        self.btn_search_all = ctk.CTkButton(self.frame_top, text="Pesquisar Tudo",
                                            corner_radius=1, width=38, height=38,
                                            command=self.search_all_items)
        self.btn_search_all.place(x=100, y=25)

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

        # Configurações de estilo da tabela
        self.tree_table.tag_configure("my_font", font=("Helvetica", 12))
        self.tree_table.tag_configure("my_bg", background="#D9E2DE")

        tree_vsb.grid(row=0, column=1, sticky="ns")
        tree_hsb.grid(row=1, column=0, sticky="ew")

        self.frame_bottom.grid_rowconfigure(0, weight=1)
        self.frame_bottom.grid_columnconfigure(0, weight=1)

        # Configuração das colunas
        header = ["nw", "nw", "nw", "nw", "ne", "ne", "center"]
        column_width = [50, 275, 180, 110, 130, 130, 110]

        for i, col in enumerate(table_header):
            from tkinter import CENTER
            self.tree_table.heading(col, text=col.title(), anchor=CENTER)
            self.tree_table.column(col, width=column_width[i], anchor=header[i])

        # Inserir itens na tabela (exemplo)
        for i, item in enumerate(self.lista):
            tags = ("my_font", "my_bg" if i % 2 == 0 else "")
            self.tree_table.insert("", "end", values=item, tags=tags)

    def search_or_export(self):
        option = self.label_search_option.get()
        query = self.label_entry_search.get()

        if option == "Produto":
            self.execute_query("SELECT * FROM stock WHERE product_name ILIKE %s", ('%' + query + '%',))
        elif option == "ID":
            try:
                query_id = int(query)
                self.execute_query("SELECT * FROM stock WHERE id = %s", (query_id,))
            except ValueError:
                self.display_no_results()
        elif option == "Data":
            self.execute_query("SELECT * FROM stock WHERE date_product = %s", (query,))
        else:
            self.display_no_results()

    def execute_query(self, sql_query, params=None):
        try:
            if params:
                self.cursor.execute(sql_query, params)
            else:
                self.cursor.execute(sql_query)
            filtered_items = self.cursor.fetchall()

            if filtered_items:
                self.display_results(filtered_items)
            else:
                self.display_no_results()
        except Exception as e:
            print(f"Erro ao executar consulta: {e}")
            self.display_no_results()

    def display_results(self, items):
        # Limpar resultados anteriores
        for item in self.tree_table.get_children():
            self.tree_table.delete(item)

        # Exibir novos resultados
        for item in items:
            self.tree_table.insert("", "end", values=item)

    def display_no_results(self):
        # Limpar resultados anteriores
        for item in self.tree_table.get_children():
            self.tree_table.delete(item)

        # Exibir mensagem de nenhum resultado encontrado
        self.tree_table.insert("", "end", values=("Nenhum resultado encontrado.",))

    def show_all_items(self):
        self.execute_query("SELECT * FROM stock")

    def search_all_items(self):
        self.execute_query("SELECT * FROM stock")

    def export_logs(self):
        option = self.label_search_option.get()
        query = self.label_entry_search.get()

        if option == "Produto":
            self.execute_export_query("SELECT * FROM stock WHERE product_name ILIKE %s", ('%' + query + '%',))
        elif option == "ID":
            try:
                query_id = int(query)
                self.execute_export_query("SELECT * FROM stock WHERE id = %s", (query_id,))
            except ValueError:
                print("ID inválido. Exportação cancelada.")
        elif option == "Data":
            self.execute_export_query("SELECT * FROM stock WHERE date_product = %s", (query,))
        else:
            print("Opção de busca inválida. Exportação cancelada.")

    def execute_export_query(self, sql_query, params=None):
        try:
            if params:
                self.cursor.execute(sql_query, params)
            else:
                self.cursor.execute(sql_query)
            filtered_items = self.cursor.fetchall()

            if filtered_items:
                with open("exported_logs.txt", "w") as file:
                    for item in filtered_items:
                        file.write(f"ID: {item[0]}, Produto: {item[1]}, Quantidade: {item[2]},"
                                   f" Preço por Unidade: {item[3]}, Preço Total: {item[4]}, Data: {item[5]}\n")

                print("Logs exportados com sucesso para 'exported_logs.txt'.")
            else:
                print("Nenhum item encontrado para exportar.")
        except Exception as e:
            print(f"Erro ao exportar logs: {e}")
