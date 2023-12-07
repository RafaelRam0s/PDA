from tkinter import *

agendar_consulta = Tk()
agendar_consulta.title("Agendar Consulta") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = agendar_consulta.winfo_screenwidth()
altura_screen = agendar_consulta.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
agendar_consulta.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(agendar_consulta, text="AGENDAMENTO DE CONSULTA", font="Monospace 20 bold").pack()

Label(agendar_consulta, text="Indentificador Paciente:", font="Monospace 12").pack()
text_indentificador_paciente = Entry(agendar_consulta)
text_indentificador_paciente.pack()

Label(agendar_consulta, text="Indentificador Médico:", font="Monospace 12").pack()
text_indentificador_medico = Entry(agendar_consulta)
text_indentificador_medico.pack()

Label(agendar_consulta, text="Data e Hora da Consulta:", font="Monospace 12").pack()
datetime_data = Entry(agendar_consulta)
datetime_data.pack()

def agendar_Consulta(paciente, medico, data):
    print(
        "Cadastro:",
        paciente, medico, data  
    )
btn_agendar_consulta = Button(agendar_consulta, text="Agendar Consulta", command=lambda: agendar_Consulta(text_indentificador_paciente.get(), text_indentificador_medico.get(), datetime_data.get())).pack()

agendar_consulta.mainloop()
