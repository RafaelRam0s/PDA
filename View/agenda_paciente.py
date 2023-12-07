from tkinter import *

agenda_paciente = Tk()
agenda_paciente.title("Ver Agenda do Paciente") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = agenda_paciente.winfo_screenwidth()
altura_screen = agenda_paciente.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
agenda_paciente.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(agenda_paciente, text="AGENDA DO PACIENTE", font="Monospace 20 bold").pack()

def pegar_Nome_Paciente():
    print("Olá Mundo!")
label_nome = Label(agenda_paciente, text="Nome do Paciente: ").pack()
def pegar_Consultas():
    print("Olá Mundo!")
label_tabela_consultas = Label(agenda_paciente, text="Consultas | Médico | Data e hora para realização").pack()
def pegar_Exames():
    print("Olá Mundo!")
label_tabela_exames = Label(agenda_paciente, text="Exames | Médico | Data e hora para realização").pack()

def imprimir_Agenda():
    print("Olá Mundo!")
btn_imprimir = Button(agenda_paciente, text="Imprimir", command=lambda: imprimir_Agenda()).pack()

agenda_paciente.mainloop()
