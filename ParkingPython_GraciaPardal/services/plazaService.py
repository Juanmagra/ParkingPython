from repository.plazaRepository import *
import services.tipoService as tipoService
import services.ticketService as ticketService
from datetime import date
from datetime import datetime

def allPlazas():
    return todasPlazas()
def plazaById(id):
    return  buscarPlazaPorId(id)
def addPlaza(plaza):
    return añadirPlaza(plaza)
def deletePlaza(id):
    return eliminarPlaza(id)

def asignarPlazaSinCliente(tipoPlaza):
    listaPlazasTipo = buscarPlazaPorTipo(tipoPlaza)
    plazaAsignada = Plaza
    guardada = False
    for plaza in listaPlazasTipo:
        if (not plaza.ocupada and not plaza.reservada and guardada==False):
            plaza.setOcupada = True
            plazaAsignada = plaza
            guardada = True
            tipoPlaza.setCantidadDisponible -=1
            tipoPlaza.setCantidadUsada +=1

    if not guardada:
       return False
    else:
        return plazaAsignada


def retirarSinCliente(ticket, plaza):
    ticket.setFechaSalida = datetime.now()
    plaza.setOcupada = False
    ticketService.editTicket(ticket)








