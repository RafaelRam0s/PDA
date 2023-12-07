import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import db_connection as db


def adicionar_medico(nome, crm, endereco, telefone, especialidade):
    values = (nome, crm, endereco, telefone, especialidade)
    query = f'INSERT INTO medicos(nome, crm, endereco, telefone, especialidade) VALUES {values}'
    db.execute_query(query)


def buscar_medico(id_medico):
    query = f'SELECT * FROM medicos m where m.id = {id_medico}'
    response = db.read_query(query)
    return response


def buscar_medicos():
    query = 'SELECT * FROM medicos'
    response = db.read_query(query)
    return response
