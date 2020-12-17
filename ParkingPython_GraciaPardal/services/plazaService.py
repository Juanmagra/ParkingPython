from repository.plazaRepository import *

def allPlazas():
    return todasPlazas()
def plazaById(id):
    return  buscarPlazaPorId(id)
def addPlaza(plaza):
    return añadirPlaza(plaza)
def deletePlaza(id):
    return eliminarPlaza(id)