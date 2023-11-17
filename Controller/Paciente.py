import Model.Pacientes
from Model import *


def adicionar_paciente(nome, nascimento, telefone, endereco, sexo, pagamento):
    Model.Pacientes.adicionar_paciente(nome, nascimento, telefone, endereco, sexo, pagamento)
