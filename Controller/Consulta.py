import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import Consultas

def redirecionar_Agendar_Consulta():
    with open("./View/agendar_consulta.py") as f:
        exec(f.read())

def adicionar_consulta(paciente, medico, data):
    Consultas.adicionar_consulta(paciente, medico, data)

def buscar_consultas_medico(medico):
    response = Consultas.buscar_consultas_medico(medico)
    return response

def buscar_consultas():
    response = Consultas.buscar_consultas()
    return response
