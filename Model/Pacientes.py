import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import db_connection as db


def adicionar_paciente(nome, nascimento, sexo, endereco, telefone, pagamento):
    values = (nome, nascimento, sexo, endereco, telefone, pagamento)
    query = f'INSERT INTO pacientes(nome, nascimento, sexo, endereco, telefone, pagamento) VALUES {values}'
    db.execute_query(query)

def buscar_paciente(id_paciente):
    query = f'SELECT * FROM pacientes p where p.id = {id_paciente}'
    response = db.read_query(query)
    return response


def buscar_pacientes():
    query = 'SELECT id, nome FROM pacientes'
    response = db.read_query(query)
    return response


