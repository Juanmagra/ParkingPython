import pickle

from models.models import Parking, TipoPlaza, Cliente

fichero = open('../datos/datos.pckl', 'rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
parking = lista_fichero
fichero.close()
tipos = parking.listaTipos


def todosTipos():
    return parking.listaTipos


def buscarTipoPorNombre(nombre):
    tipoNombre = TipoPlaza()
    for tipo in tipos:
        if tipo.nombre.upper() == nombre.upper():
            tipoNombre = tipo
    return tipoNombre


def buscarTipoPorId(id):
    tipoDni = TipoPlaza()
    for tipo in tipos:
        if tipo.id == id:
            tipoDni = tipo
    return tipoDni


def añadirTipo(tipo):
    tipo.setId =parking.idGenerator()
    tipos.append(tipo)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()


def eliminarTipo(id):
    tipoDel = buscarTipoPorId(id)
    tipos.remove(tipoDel)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()
