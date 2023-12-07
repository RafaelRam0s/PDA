from tkinter import *
import Paciente
import Pedido_exame

gerenciar_medico = Tk()
gerenciar_medico.title("Gerenciar Pacientes") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = gerenciar_medico.winfo_screenwidth()
altura_screen = gerenciar_medico.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
gerenciar_medico.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(gerenciar_medico, text="GERENCIAMENTO DE PACIENTES", font="Monospace 20 bold").pack()

def ver_Historico():
    Paciente.redirecionar_Agenda_Paciente()
def ver_Pacientes():
    return Paciente.buscar_pacientes()
label_tabela = Label(gerenciar_medico, text="Indentificador | Nome | Histórico de agendamentos", font="Monospace 12").pack()
label_tabela["text"] += ver_Pacientes()
gerenciar_medico.mainloop()
