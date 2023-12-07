import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import Exames

def redirecionar_Cadastrar_Exame():
    with open("./View/cadastrar_exame.py") as f:
        exec(f.read())

def redirecionar_Gerenciar_Exames():
    with open("./View/gerenciar_exame.py") as f:
        exec(f.read())

def adicionar_exame(nome, valor, orientacoes):
    Exames.adicionar_exame(nome, valor, orientacoes)

def buscar_exame(id):
    response = Exames.buscar_exame(id)
    return response

def buscar_exames():
    response = Exames.buscar_exames()
    return response
