import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import db_connection as db


def adicionar_consulta(paciente, medico, data):
    values = (paciente, medico, data)
    query = f'INSERT INTO consultas(id_paciente, id_medico, data_consulta) VALUES {values}'
    db.execute_query(query)


def buscar_consultas_medico(id_medico):
    query = f'SELECT * FROM consultas c where c.id_medico = {id_medico}'
    response = db.read_query(query)
    return response


def buscar_consultas():
    query = 'SELECT * FROM consultas'
    response = db.read_query(query)
    return response
