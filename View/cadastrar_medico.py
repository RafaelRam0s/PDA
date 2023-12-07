from tkinter import *
from tkinter.ttk import *
import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Controller')
import Especialidade
import Medico


cadastrar_medico = Tk()
cadastrar_medico.title("Cadastrar Médico") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = cadastrar_medico.winfo_screenwidth()
altura_screen = cadastrar_medico.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
cadastrar_medico.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(cadastrar_medico, text="CADASTRO MÉDICO", font="Monospace 20 bold").pack()

Label(cadastrar_medico, text="Nome Completo:", font="Monospace 12").pack()
text_nome = Entry(cadastrar_medico)
text_nome.pack()

Label(cadastrar_medico, text="Número de CRM:", font="Monospace 12").pack()
text_crm = Entry(cadastrar_medico)
text_crm.pack()

Label(cadastrar_medico, text="Endereço:", font="Monospace 12").pack()
text_endereco = Entry(cadastrar_medico)
text_endereco.pack()

Label(cadastrar_medico, text="Telefone:", font="Monospace 12").pack()
text_telefone = Entry(cadastrar_medico)
text_telefone.pack()

Label(cadastrar_medico, text="Indentificador da Especialidade:", font="Monospace 12").pack()
combo = ttk.Combobox(cadastrar_medico)
combo['values']= get_especialidades_nome()
combo.pack()

def cadastrar_Medico(nome, crm, endereco, telefone, especialidade):
    Medico.adicionar_medico(nome, crm, endereco, telefone, especialidade)

def get_especialidade_nome():
    response = []
    data = Especialidade.buscar_especialidades()
    for item in data:
        response.append(item[1])
    return response

btn_cadastrar_medico = Button(cadastrar_medico, text="Cadastrar Médico", command=lambda: cadastrar_Medico(
    text_nome.get(),
    text_crm.get(),
    text_endereco.get(),
    text_telefone.get(),
    get_especialidade_id()
)).pack()

cadastrar_medico.mainloop()
