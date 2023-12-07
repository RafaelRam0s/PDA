import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import db_connection as db


def adicionar_especialidade(nome):
    values = (nome)
    query = f'INSERT INTO pacientes(nome) VALUES {values}'
    db.execute_query(query)


def buscar_especialidades():
    query = 'SELECT * FROM especialidades'
    response = db.read_query(query)
    return response
