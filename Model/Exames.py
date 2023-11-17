import db_connection as db


def adicionar_exame(nome, valor, orientacoes):
    values = (nome, valor, orientacoes)
    query = f'INSERT INTO exames(nome, valor, orientacoes) VALUES {values}'


def buscar_exame(id_exame):
    query = f'SELECT * FROM exames p where p.id = {id_exame}'
    response = db.read_query(query)
    return response


def buscar_exames():
    query = 'SELECT * FROM exames'
    response = db.read_query(query)
    return response
