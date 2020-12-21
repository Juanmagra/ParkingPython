import pickle

from models.models import Parking, Cliente

fichero = open('datos/datos.pckl', 'rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
parking = Parking();
parking = lista_fichero
fichero.close()


def todosClientes():
    return parking.listaUsuarios


def buscarClientePorDni(dni):
    clientes = parking.listaUsuarios
    clienteDni = Cliente()
    for cliente in clientes:
        if (cliente.dni == dni):
            clienteDni = cliente
    return clienteDni




def añadirCliente(cliente):
    clientes = parking.listaUsuarios
    clientes.append(cliente)
    fichero = open('datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()


def eliminarCliente(dni):
    clientes = parking.listaUsuarios
    clienteDel = buscarClientePorDni(dni)
    clientes.remove(clienteDel)
    fichero = open('datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()
