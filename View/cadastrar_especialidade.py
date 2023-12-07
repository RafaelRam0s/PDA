from tkinter import *

cadastrar_especialidade = Tk()
cadastrar_especialidade.title("Cadastrar Especialidade") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = cadastrar_especialidade.winfo_screenwidth()
altura_screen = cadastrar_especialidade.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
cadastrar_especialidade.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(cadastrar_especialidade, text="CADASTRO DE ESPECIALIDADE", font="Monospace 20 bold").pack()

label_indentificador = Label(cadastrar_especialidade, text="Indentificador:", font="Monospace 12").pack()
text_indentificador = Entry(cadastrar_especialidade)
text_indentificador.pack()

label_nome = Label(cadastrar_especialidade, text="Nome:", font="Monospace 12").pack()
text_nome = Entry(cadastrar_especialidade)
text_nome.pack()

def cadastrar_Especialidade(indentificador, nome):
    print(
        "Cadantro",
        indentificador, nome
    )
btn_cadastrar_especialidade = Button(cadastrar_especialidade, text="Cadastrar Especialidade", command=lambda: cadastrar_Especialidade(text_indentificador.get(), text_nome.get())).pack()

cadastrar_especialidade.mainloop()
