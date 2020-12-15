import pickle

from models.models import Parking, TipoPlaza

fichero = open('../datos/datos.pckl','rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
parking = Parking();
parking = lista_fichero

for i in parking.listaTipos:
    print(i)


fichero.close()