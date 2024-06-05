import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Olá! Este é um exemplo de aplicação Tkinter.")

#Criar janela principal
root = tk.Tk()
root.title("Exemplo Tkinter")

#Criar rótulo
label = tk.Label(root, text="Clique no botão para mostrar uma mensagem.")
label.pack(pady=10)

#Criar botão
button = tk.Button(root, text="Mostrar Mensagem", command=mostrar_mensagem)
button.pack()

#Executar o loop principal da aplicação
root.mainloop()