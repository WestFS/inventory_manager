import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk


def check_login(username, password):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')


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

    login_window = ctk.CTk()
    window_width, window_height = 300, 180
    center_window(login_window, window_width, window_height)
    login_window.title("LOGIN")

    login_frame = ctk.CTkFrame(login_window)
    login_frame.pack(padx=10, pady=10)

    username_label = ctk.CTkLabel(login_frame, text="username")
    username_label.grid(row=0, column=0, padx=5, pady=5)

    username_entry = ctk.CTkEntry(login_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = ctk.CTkLabel(login_frame, text="password")
    password_label.grid(row=1, column=0, padx=5, pady=5)

    password_entry = ctk.CTkEntry(login_frame, show='*')
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    toggle_button = ctk.CTkButton(login_frame, text="Mostrar Senha", command=toggle_password_visibility)
    toggle_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    login_button = ctk.CTkButton(login_frame, text="Login", command=attempt_login)
    login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


    login_window.mainloop()

if __name__ == "__main__":
    login_screen()
