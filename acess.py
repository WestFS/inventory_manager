import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from PIL import Image
from screen_inventory.main_screen import Screen
from database.connection_db import connect_to_db


def check_login(username, password):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry(f"+{x}+{y}")


def open_main_screen():
    main_screen = Screen()
    main_screen.open_main_screen()  # Exibe a tela principal do main_screen.py


def login_screen():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()

        if check_login(username, password):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            login_window.destroy()  # Fecha a janela de login
            open_main_screen()

        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def toggle_password_visibility():
        if password_entry.cget('show') == '*':
            password_entry.configure(show='')
            toggle_button.configure(image=eye_closed_ctk_image)
        else:
            password_entry.configure(show='*')
            toggle_button.configure(image=eye_open_ctk_image)

    login_window = ctk.CTk()
    login_window.geometry("720x450")
    login_window.resizable(False, False)
    login_window.title("LOGIN")

    eye_open_image = Image.open("image/eye.png")
    eye_open_ctk_image = ctk.CTkImage(light_image=eye_open_image, size=(20, 20))
    eye_closed_image = Image.open("image/eye-slash.png")
    eye_closed_ctk_image = ctk.CTkImage(light_image=eye_closed_image, size=(20, 20))

    icon_user = Image.open("image/icon_login.png")
    icon_user_ctk_image = ctk.CTkImage(light_image=icon_user, size=(125, 125))

    frame_left = ctk.CTkFrame(login_window, width=360, height=450, fg_color="purple")
    frame_left.grid(row=1, column=0, sticky="nsew")

    frame_right = ctk.CTkFrame(login_window, width=360, height=450)
    frame_right.grid(row=1, column=2, rowspan=2, sticky="nsew")

    icon_label = ctk.CTkLabel(frame_right, image=icon_user_ctk_image, text="")
    icon_label.place(x=180, y=60, anchor="center")

    username_label = ctk.CTkLabel(frame_right, text="Username")
    username_label.place(x=180, y=135, anchor="center")

    username_entry = ctk.CTkEntry(frame_right)
    username_entry.place(x=180, y=160, anchor="center")

    password_label = ctk.CTkLabel(frame_right, text="Password")
    password_label.place(x=180, y=200, anchor="center")

    password_entry = ctk.CTkEntry(frame_right, show='*')
    password_entry.place(x=180, rely=0.5, anchor="center")

    toggle_button = ctk.CTkButton(frame_right, text="", image=eye_open_ctk_image, command=toggle_password_visibility,
                                  fg_color="transparent", width=2, height=2)
    toggle_button.place(x=265, rely=0.5, anchor="center")

    login_button = ctk.CTkButton(frame_right, text="Login", command=attempt_login, fg_color="purple")
    login_button.place(x=180, rely=0.6, anchor="center")

    center_window(login_window)
    login_window.mainloop()


if __name__ == "__main__":
    login_screen()
