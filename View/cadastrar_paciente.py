from tkinter import *
import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Controller')
from .Controller import Paciente

cadastrar_paciente = Tk()
cadastrar_paciente.title("Cadastrar Paciente") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = cadastrar_paciente.winfo_screenwidth()
altura_screen = cadastrar_paciente.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
cadastrar_paciente.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(cadastrar_paciente, text="CADASTRO PACIENTE", font="Monospace 20 bold").pack()

Label(cadastrar_paciente, text="Nome Completo:", font="Monospace 12").pack()
text_nome = Entry(cadastrar_paciente)
text_nome.pack()

Label(cadastrar_paciente, text="Foto:", font="Monospace 12").pack()
text_foto = Entry(cadastrar_paciente)
text_foto.pack()

Label(cadastrar_paciente, text="Data de nascimento:", font="Monospace 12").pack()
datetime_data_nascimento = Entry(cadastrar_paciente)
datetime_data_nascimento.pack()

Label(cadastrar_paciente, text="Sexo:", font="Monospace 12").pack()
text_sexo = Entry(cadastrar_paciente)
text_sexo.pack()

Label(cadastrar_paciente, text="Endereço:", font="Monospace 12").pack()
text_endereco = Entry(cadastrar_paciente)
text_endereco.pack()

Label(cadastrar_paciente, text="Telefone:", font="Monospace 12").pack()
text_telefone = Entry(cadastrar_paciente)
text_telefone.pack()

Label(cadastrar_paciente, text="Forma de Pagamento:", font="Monospace 12").pack()
text_forma_de_pagamento = Entry(cadastrar_paciente)
text_forma_de_pagamento.pack()


def cadastrar_Paciente(nome, data, telefone, endereco, sexo, pagamento):
    Paciente.adicionar_paciente(nome, data,  sexo, endereco, telefone, pagamento)

btn_cadastrar_paciente = Button(cadastrar_paciente, text="Cadastrar Paciente", command=lambda: Paciente.adicionar_paciente(text_nome.get(), datetime_data_nascimento.get(), text_telefone.get(), text_endereco.get(), text_sexo.get(), text_forma_de_pagamento.get())).pack()




cadastrar_paciente.mainloop()
