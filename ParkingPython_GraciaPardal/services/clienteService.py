from repository.clienteRepository import *


def allClientes():
    return todosClientes()


def clientePorDni(dni):
    return buscarClientePorDni(dni)


def deleteCliente(dni):
    eliminarCliente(dni)

def addCliente(cliente):
    añadirCliente(cliente)
