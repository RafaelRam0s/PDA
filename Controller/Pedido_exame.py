import sys
sys.path.append('C:\\Users\\rafae\\OneDrive\\Documentos\\GitHub\\PDA\\Model')
import pedidos_exames

def adicionar_pedido(codigo, paciente, medico, data, valor):
    Model.pedidos_exames.adicionar_pedidos_exames(codigo, paciente, medico, data, valor)

def buscar_pedidos():
     response = Model.Pacientes.buscar_pedidos_exames()
     return response

def buscar_pedido(id):
     response = Model.Pacientes.buscar_pedido_exame(id)
     return response