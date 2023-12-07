import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import db_connection as db


def adicionar_pedidos_exames(codigo, paciente, medico, data_exame, valor_pago):
    values = (codigo, paciente, medico, data_exame, valor_pago)
    query = f'INSERT INTO pedidos_examess(codigo, paciente, medico, data_exame, valor_pago) VALUES {values}'
    db.execute_query(query)


def buscar_pedido_exame(id_pedidos_exames):
    query = f'SELECT * FROM pedidos_examess p where p.id = {id_pedidos_exames}'
    response = db.read_query(query)
    return response


def buscar_pedidos_exames():
    query = 'SELECT * FROM pedidos_examess'
    response = db.read_query(query)
    return response
