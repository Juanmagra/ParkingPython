import pickle

from models.models import Parking, Plaza

fichero = open('datos/datos.pckl', 'rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
parking = Parking();
parking = lista_fichero
fichero.close()
plazas = parking.listaPlazas


def todasPlazas():
    return parking.listaPlazas


def buscarPlazaPorTipo(tipo):
    plazaPorTipo = [Plaza]
    for plaza in parking.listaPlazas:
        if tipo.nombre == plaza.tipoPlaza:
            plazaPorTipo.append(plaza)
    return plazaPorTipo


def buscarPlazaPorId(id):
    plazaId = Plaza()
    for plaza in plazas:
        if plaza.id == id:
            plazaId = plaza

    if plaza.id == 0:
        return False
    else:
        return plazaId


def añadirPlaza(plaza):
    if plaza.id=='0':
         plaza.setId = parking.idGenerator()
    plazas.append(plaza)
    fichero = open('datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()

def eliminarPlaza(id):
    plazaDel = buscarPlazaPorId(id)
    plazas.remove(plazaDel)
    fichero = open('datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()

def editarPlaza(plaza):
    eliminarPlaza(plaza.id)
    añadirPlaza(plaza)
    fichero = open('datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()