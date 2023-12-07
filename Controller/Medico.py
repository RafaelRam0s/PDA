import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import Medicos

def redirecionar_Cadastrar_Medico():
    with open("./View/cadastrar_medico.py") as f:
        exec(f.read())

def redirecionar_Gerenciar_Medicos():
    with open("./View/gerenciar_medico.py") as f:
        exec(f.read())

def redirecionar_Agenda_Medico():
    with open("./View/agenda_medico.py") as f:
        exec(f.read())

def adicionar_medico(nome, crm, endereco, telefone, especialidade):
    Medicos.adicionar_medico(nome, crm, endereco, telefone, especialidade)

def buscar_medicos():
    response = Medicos.buscar_medicos()
    return response

def buscar_paciente(id_medico):
    response = Medicos.buscar_paciente(id_medico)
    return response