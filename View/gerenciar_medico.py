from tkinter import *
import Medico
import Consulta
gerenciar_medico = Tk()
gerenciar_medico.title("Gerenciar Médicos") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = gerenciar_medico.winfo_screenwidth()
altura_screen = gerenciar_medico.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
gerenciar_medico.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(gerenciar_medico, text="GERENCIAMENTO DE MÉDICOS", font="Monospace 20 bold").pack()

def ver_Agenda():
    Medico.redirecionar_Agenda_Medico()
def ver_Medicos():
    return Medico.buscar_medicos()
label_tabela = Label(gerenciar_medico, text="Indentificador | Nome | CRM | Endereço | Telefone | Especialidade | Agenda:", font="Monospace 12").pack()
label_tabela["text"] += ver_Medicos()

gerenciar_medico.mainloop()
