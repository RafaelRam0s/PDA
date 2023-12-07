import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import Pacientes

def redirecionar_Cadastrar_Paciente():
    with open("./View/cadastrar_paciente.py") as f:
        exec(f.read())

def redirecionar_Gerenciar_Pacientes():
    with open("./View/gerenciar_paciente.py") as f:
        exec(f.read())

def redirecionar_Cadastrar_Paciente():
    with open("./View/cadastrar_paciente.py") as f:
        exec(f.read())

def cadicionar_paciente(nome, nascimento, sexo, endereco, telefone, pagamento):
    adicionar_paciente(nome, nascimento, sexo, endereco, telefone, pagamento)

def cbuscar_pacientes():
    response = buscar_pacientes()
    return response

def cbuscar_paciente(id_paciente):
    response = buscar_paciente(id_paciente)
    return response