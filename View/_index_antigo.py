from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from datetime import date

import Controller.Paciente
from Controller import *


class Application:
    def __init__(self, master=None):
        pass


def adicionar_paciente_window():
    new_window = Toplevel(root)
    new_window.title("Adicionar Paciente")
    new_window.geometry("400x400")

    nome_label = Label(new_window, text="Nome Completo:")
    nome_label.grid(column=0, row=0)
    nome_label = Entry(new_window)
    nome_label.grid(column=0, row=1, columnspan=2)

    endereco_label = Label(new_window, text="Endereço:")
    endereco_label.grid(column=0, row=2)
    endereco_label = Entry(new_window)
    endereco_label.grid(column=0, row=3, columnspan=2)

    telefone_label = Label(new_window, text="Telefone:")
    telefone_label.grid(column=0, row=4)
    telefone_label = Entry(new_window)
    telefone_label.grid(column=0, row=5, columnspan=2)

    nascimento_label = Label(new_window, text="Data de Nascimento(dd/mm/yyyy):")
    nascimento_label.grid(column=2, row=0)
    nascimento_label = Entry(new_window)
    nascimento_label.grid(column=2, row=1)

    sexo_label = Label(new_window, text="Sexo(M/F):")
    sexo_label.grid(column=2, row=4)
    sexo_label = Entry(new_window)
    sexo_label.grid(column=2, row=5)

    pagamento_label = Label(new_window, text="Forma de Pagamento:")
    pagamento_label.grid(column=2, row=2)
    pagamento_label = Entry(new_window)
    pagamento_label.grid(column=2, row=3)

    def adicionar_paciente_action():
        nome = nome_label.get()
        endereco = endereco_label.get()
        telefone = telefone_label.get()
        nascimento = nascimento_label.get()
        sexo = sexo_label.get()
        pagamento = pagamento_label.get()
        Controller.Paciente.adicionar_paciente(nome, nascimento, telefone, endereco, sexo, pagamento)

    confirmar = ttk.Button(new_window, text="Adicionar paciente", default="active", command=adicionar_paciente_action)
    confirmar.grid(column=0, row=6)

root = Tk()
root.title("Clínica")
root.geometry("400x400")

add_paciente = ttk.Button(root, text="Adicionar Paciente", default="active", command=adicionar_paciente_window)
add_paciente.grid(column=0, row=0)
Application(root)
root.mainloop()
