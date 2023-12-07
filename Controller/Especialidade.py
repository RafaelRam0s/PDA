import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import Especialidades

def redirecionar_Cadastrar_Especialidade():
    with open("./View/cadastrar_especialidade.py") as f:
        exec(f.read())

def adicionar_especialidade(nome):
    Especialidades.adicionar_especialidade(nome)

def buscar_especialidades():
    response = Especialidades.buscar_especialidades()
    return response