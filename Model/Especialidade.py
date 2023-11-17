import db_connection as db


def adicionar_especialidade(nome):
    values = (nome)
    query = f'INSERT INTO pacientes(nome) VALUES {values}'



def buscar_especialidade():
    query = 'SELECT * FROM especialidades'
    response = db.read_query(query)
    return response
