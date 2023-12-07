from tkinter import *
import Exame
gerenciar_medico = Tk()
gerenciar_medico.title("Gerenciar Exames") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = gerenciar_medico.winfo_screenwidth()
altura_screen = gerenciar_medico.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
gerenciar_medico.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(gerenciar_medico, text="GERENCIAMENTO DE EXAMES", font="Monospace 20 bold").pack()

def imprimir_Exame(id):
    print(Exame.buscar_exame(id))
def ver_Medicos():
    return Exame.buscar_exames()
label_tabela = Label(gerenciar_medico, text="Indentificador | Nome | Valor | Orientação | Paciente | Médico | Data | Imprimir", font="Monospace 12").pack()
label_tabela["text"] += ver_Medicos()

gerenciar_medico.mainloop()
