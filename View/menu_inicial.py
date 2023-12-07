from tkinter import *
import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Controller')
from Paciente import redirecionar_Cadastrar_Paciente
from Paciente import redirecionar_Gerenciar_Pacientes
from Medico import redirecionar_Cadastrar_Medico
from Medico import redirecionar_Gerenciar_Medicos
from Exame import redirecionar_Cadastrar_Exame
from Exame import redirecionar_Gerenciar_Exames
from Especialidade import redirecionar_Cadastrar_Especialidade
from Consulta import redirecionar_Agendar_Consulta

menu_inicial = Tk()
menu_inicial.title("Menu inicial") # define o titulo do aplicativo

largura = 800
altura = 600
largura_screen = menu_inicial.winfo_screenwidth()
altura_screen = menu_inicial.winfo_screenheight()
posx = (largura_screen/2) - (largura/2)
posy = (altura_screen/2) - (altura/2)
menu_inicial.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


label_titulo = Label(menu_inicial, text="Menu", font="Monospace 20 bold").pack()

def redirecionar_CadastrarPaciente():
    redirecionar_Cadastrar_Paciente()
btn_cadastrar_paciente = Button(menu_inicial, text="Cadastrar Paciente", command=lambda: redirecionar_CadastrarPaciente()).pack()

def redirecionar_CadastrarEspecialidade():
    redirecionar_Cadastrar_Especialidade()
btn_cadastrar_especialidade = Button(menu_inicial, text="Cadastrar Epecialidade", command=lambda: redirecionar_CadastrarEspecialidade()).pack()

def redirecionar_CadastrarMedico():
    redirecionar_Cadastrar_Medico()
btn_cadastrar_medico = Button(menu_inicial, text=u"Cadastrar M\u00e9dico", command=lambda: redirecionar_CadastrarMedico()).pack()

def redirecionar_CadastrarExame():
    redirecionar_Cadastrar_Exame()
btn_cadastrar_exame = Button(menu_inicial, text="Cadastrar Exame", command=lambda: redirecionar_CadastrarExame()).pack()

def redirecionar_AgendarConsulta():
    redirecionar_Agendar_Consulta()
btn_agendar_consulta = Button(menu_inicial, text="Agendar Consulta", command=lambda: redirecionar_AgendarConsulta()).pack()

def redirecionar_GerenciarMedicos():
    redirecionar_Gerenciar_Medicos()
btn_gerenciar_medicos = Button(menu_inicial, text="Gerenciar Médicos", command=lambda: redirecionar_GerenciarMedicos()).pack()

def redirecionar_GerenciarExames():
    redirecionar_Gerenciar_Exames()
btn_gerenciar_exames = Button(menu_inicial, text="Gerenciar Exames", command=lambda: redirecionar_GerenciarExames()).pack()

def redirecionar_GerenciarPacientes():
    redirecionar_Gerenciar_Pacientes()
btn_gerenciar_pacientes = Button(menu_inicial, text="Gerenciar Pacientes", command=lambda: redirecionar_GerenciarPacientes()).pack()

menu_inicial.mainloop()


