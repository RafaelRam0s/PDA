from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Menu inicial") # define o titulo do aplicativo

# menu_inicial.geometry("800x600+400+100") # define o tamanho da janela e a posição inicial que irá surgir
# menu_inicial.resizable(True, True)

# menu_inicial.resizable(False, False) # não permite redimensionamento da tela clicando nos cantos
# menu_inicial.minsize(300, 200) # define e mínima largura e a minima altua que a janela pode chegar
# menu_inicial.maxsize(1000, 800) # define e máxima largura e a máxima altura que a janela pode chegar
# menu_inicial.state("zoomed") # inicia a janela cobrindo toda a tela
# menu_inicial.state("iconic") # inicia a janela minimizada
# menu_inicial.iconbitmap("images/icon.ico") # modifica o ícone do aplicativo se tivesse uma pasta com images e o arquivo de icone
# menu_inicial['bg'] = "blue" # muda a cor de fundo do aplicativo para azul

# botao com evento de click, soltando a mensagem no console
# def cmd_Click():
#     print("Olá Mundo!")
# btn1 = Button(menu_inicial, text="Teste", command=lambda: cmd_Click())
# btn1.pack()

largura = 800
altura = 600
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
# print(largura_screen, altura_screen)
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

# inserindo textos
# label_1 = Label(menu_inicial, text = "Olá mundo")
# label_1.pack()
# label_2 = Label(menu_inicial, text = "Teste 2")
# label_2.pack()

# mexendo com o estilo em texto
# label_teste = Label(
#     menu_inicial, 
#     text="Testando os estilos",
#     font="Monospace 18 bold italic",
#     bg="#ff4d4d",
#     fg="black"
# )
# Alguns outros parametros: print(label_teste.keys()) | comando para ver tudo o que esta configurado for item in label_teste.keys(): print(item, " : ", label_teste[item])
# width=20 que aumenta a largura da caixa com base no tamanho da fonte do label
# padx=10 pady=15 aumenta o padding em pixels
# justify=CENTER LEFT RIGHT como o texto se ajusta com múltiplas linhas
# borderwidth=1 relief="solid" fazer a borda de um elemento
# anchor=NW que posiciona o texto em um ponto cardial dentro da caixa já que o padrão é no centro
# label_teste.pack()

# modificar por um texto labels diferentes
# texto = StringVar()
# texto.set("Novo texto")
# label_1 = Label(menu_inicial, textvariable=texto)
# label_1.pack()
# label_2 = Label(menu_inicial, textvariable=texto)
# label_2.pack()
# texto.set("Outro texto")



menu_inicial.mainloop()
