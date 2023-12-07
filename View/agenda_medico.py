from tkinter import *

agenda_medico = Tk()
agenda_medico.title("Ver Agenda do Médico") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = agenda_medico.winfo_screenwidth()
altura_screen = agenda_medico.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
agenda_medico.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(agenda_medico, text="AGENDA DO MÉDICO", font="Monospace 20 bold").pack()

def pegar_Consultas():
    print("Olá Mundo!")
label_tabela_consultas = Label(agenda_medico, text="Consultas | Paciente | Data e hora para realização").pack()
def pegar_Exames():
    print("Olá Mundo!")
label_tabela_exames = Label(agenda_medico, text="Exames | Paciente | Data e hora para realização").pack()

def imprimir_Agenda():
    print("Olá Mundo!")
btn_imprimir = Button(agenda_medico, text="Imprimir", command=lambda: imprimir_Agenda()).pack()

agenda_medico.mainloop()
