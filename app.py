import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from connection import connect_to_db
from PIL import Image, ImageTk

# Função para verificar login
def check_login(username, password):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# Função para centralizar a janela
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Função para a tela de login
def login_screen():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()
        
        if check_login(username, password):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            login_window.destroy()  # Fecha a janela de login
            main_screen()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
    
    def toggle_password_visibility():
        if password_entry.cget('show') == '*':
            password_entry.config(show='')
            toggle_button.config(image=eye_closed_image)
        else:
            password_entry.config(show='*')
            toggle_button.config(image=eye_open_image)
    
    login_window = ttk.Window(themename="superhero")
    login_window.title("Login")
    window_width, window_height = 300, 180
    center_window(login_window, window_width, window_height)  # Centraliza a janela de login

    # Carrega as imagens dos ícones
    eye_open_image = ImageTk.PhotoImage(Image.open("eye.png").resize((20, 20)))
    eye_closed_image = ImageTk.PhotoImage(Image.open("eye-slash.png").resize((20, 20)))

    # Cria um frame para centralizar o conteúdo
    frame = ttk.Frame(login_window)
    frame.grid(row=0, column=0, sticky="nsew")
    login_window.grid_rowconfigure(0, weight=1)
    login_window.grid_columnconfigure(0, weight=1)

    ttk.Label(frame, text="Username").grid(row=0, column=0, padx=10, pady=10, sticky="e")
    username_entry = ttk.Entry(frame)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    ttk.Label(frame, text="Password").grid(row=1, column=0, padx=10, pady=10, sticky="e")
    password_entry = ttk.Entry(frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Cria um estilo personalizado para o botão de alternância
    style = ttk.Style()
    style.configure("TButton", background="white", borderwidth=0)
    style.map("TButton",
              background=[('active', 'white')],
              relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

    toggle_button = ttk.Button(frame, image=eye_open_image, command=toggle_password_visibility, bootstyle=SECONDARY, style="TButton", padding=(1, 1))
    toggle_button.grid(row=1, column=2, padx=10, pady=10)

    ttk.Button(frame, text="Login", command=attempt_login, bootstyle=SUCCESS).grid(row=2, column=0, columnspan=3, pady=10)

    login_window.mainloop()

# Função para a tela principal após login bem-sucedido
def main_screen():
    main_window = ttk.Window(themename="superhero")
    main_window.title("Tela Principal")
    window_width, window_height = 400, 300
    center_window(main_window, window_width, window_height)  # Centraliza a janela principal

    ttk.Label(main_window, text="Bem-vindo!", bootstyle=INFO).pack(pady=20)

    main_window.mainloop()

if __name__ == "__main__":
    login_screen()
