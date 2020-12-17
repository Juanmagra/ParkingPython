import pickle

from models.models import Parking, TipoPlaza, Cliente, Plaza

fichero = open('../datos/datos.pckl','rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
parking = Parking();
parking = lista_fichero
fichero.close()
plazas = parking.listaPlazas


def todasPlazas():
    return parking.listaPlazas

def buscarPlazaPorId(id):
    plazaId =Plaza()
    for plaza in plazas:
        if plaza.id == id:
            plazaId = plaza
    return plazaId

def añadirPlaza(plaza):
    idPlaza = parking.idGenerator()
    print(type(idPlaza))
    plaza.setId(idPlaza)
    plazas.append(plaza)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()

def eliminarPlaza(id):
    plazaDel = buscarPlazaPorId(id)
    plazas.remove(plazaDel)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()