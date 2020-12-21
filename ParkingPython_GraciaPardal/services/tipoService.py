from repository.tipoPlazaRepository import *


def allTipos():
    return todosTipos()


def tipoPorNombre(nombre):
    return buscarTipoPorNombre(nombre)


def tipoPorId(id):
    return buscarTipoPorId(id)


def addTipo(tipo):
    return añadirTipo(tipo)


def deleteTipo(id):
    return eliminarTipo(id)
