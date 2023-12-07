from tkinter import *

cadastrar_exame = Tk()
cadastrar_exame.title("Cadastrar Exame") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = cadastrar_exame.winfo_screenwidth()
altura_screen = cadastrar_exame.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
cadastrar_exame.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(cadastrar_exame, text="CADASTRO DE EXAME MÉDICO", font="Monospace 20 bold").pack()

Label(cadastrar_exame, text="Indentificador:", font="Monospace 12").pack()
text_indentificador = Entry(cadastrar_exame)
text_indentificador.pack()

Label(cadastrar_exame, text="Nome:", font="Monospace 12").pack()
text_nome = Entry(cadastrar_exame)
text_nome.pack()

Label(cadastrar_exame, text="Valor em Reais:", font="Monospace 12").pack()
text_valor = Entry(cadastrar_exame)
text_valor.pack()

Label(cadastrar_exame, text="Orientações sobre o exame:", font="Monospace 12").pack()
text_orientacoes = Entry(cadastrar_exame)
text_orientacoes.pack()

Label(cadastrar_exame, text="Indentificador Paciente:", font="Monospace 12").pack()
text_indentificador_paciente = Entry(cadastrar_exame)
text_indentificador_paciente.pack()

Label(cadastrar_exame, text="Indentificador Médico:", font="Monospace 12").pack()
text_indentificador_medico = Entry(cadastrar_exame)
text_indentificador_medico.pack()

Label(cadastrar_exame, text="Data e Hora do Exame:", font="Monospace 12").pack()
text_data = Entry(cadastrar_exame)
text_data.pack()


def cadastrar_Exame(text_indentificador,
text_nome,
text_valor,
text_orientacoes,
text_indentificador_paciente,
text_indentificador_medico,
text_data):
    print("Cadastro:",
        text_indentificador,
        text_nome,
        text_valor,
        text_orientacoes,
        text_indentificador_paciente,
        text_indentificador_medico,
        text_data
    )
btn_cadastrar_exame = Button(cadastrar_exame, text="Cadastrar Exame", command=lambda: cadastrar_Exame(
    text_indentificador.get(),
    text_nome.get(),
    text_valor.get(),
    text_orientacoes.get(),
    text_indentificador_paciente.get(),
    text_indentificador_medico.get(),
    text_data.get()
)).pack()

cadastrar_exame.mainloop()
