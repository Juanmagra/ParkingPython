from datetime import datetime

import services.ticketService as ticketService
from models.models import Moto, Minusvalido, Turismo, Plaza
import repository.plazaRepository as plazaRpository
import repository.tipoPlazaRepository as tipoPlazaRepo




def allPlazas():
    return plazaRpository.todasPlazas()


def plazaById(id):
    return plazaRpository.buscarPlazaPorId(id)


def addPlaza(plaza):
    return plazaRpository.añadirPlaza(plaza)


def deletePlaza(id):
    return plazaRpository.eliminarPlaza(id)

def editarPlaza(plaza):
    return plazaRpository.editarPlaza(plaza)

def asignarPlazaSinCliente(tipoPlaza):
    listaPlazasTipo = plazaRpository.buscarPlazaPorTipo(tipoPlaza)
    plazaAsignada = Plaza()
    idPlaza = ''
    guardada = False
    for plaza in listaPlazasTipo:
        if  (plaza.ocupada==False and plaza.reservada==False and guardada == False):
            plaza.setOcupada = True
            plazaAsignada = plaza
            guardada = True
            idPlaza = plaza.id
            tipoPlaza.setCantidadDisponible -= 1
            tipoPlaza.setCantidadUsada += 1
            tipoPlazaRepo.editarTipo(tipoPlaza)

    if not guardada:
        return False
    else:
        plazaRpository.editarPlaza(plazaAsignada)
        return plazaAsignada


def retirarSinCliente(ticket, plaza):
    ticket.setFechaSalida = datetime.now()
    total = ticketService.calcularTotal(ticket)
    ticket.setPrecioFinal = total
    plaza.setOcupada = False
    plazaRpository.editarPlaza(plaza)
    tipoPlaza = tipoPlazaRepo.buscarTipoPorNombre(plaza.tipoPlaza)
    tipoPlaza.setCantidadDisponible +=1
    tipoPlaza.setCantidadUsada -= 1
    tipoPlazaRepo.editarTipo(tipoPlaza)
    ticketService.editTicket( ticket)


def asignarPlazaCliente(vehiculo):
    listaPlazas = [Plaza]
    if isinstance(vehiculo, Moto):
        listaPlazas = plazaRpository.buscarPlazaPorTipo(tipoPlazaRepo.buscarTipoPorNombre("MOTO"))

    if isinstance(vehiculo, Turismo):
        listaPlazas = plazaRpository.buscarPlazaPorTipo(tipoPlazaRepo.buscarTipoPorNombre("TURISMO"))

    if isinstance(vehiculo, Minusvalido):
        listaPlazas = plazaRpository.buscarPlazaPorTipo(tipoPlazaRepo.buscarTipoPorNombre("MINUSVALIDO"))


    plazaAsignada = None
    guardada = False
    for plaza in listaPlazas:
        if plaza.ocupada == False and plaza.reservada == False and guardada == False:
            plaza.setReservada = True
            plazaAsignada = plaza
            guardada = True
            tipoPlaza = tipoPlazaRepo.buscarTipoPorNombre(plaza.tipoPlaza)
            tipoPlaza.setCantidadDisponible -= 1
            tipoPlaza.setCantidadReserved += 1
            tipoPlazaRepo.editarTipo(tipoPlaza)

    if guardada == False:
        return False
    else:
        plazaRpository.editarPlaza(plazaAsignada)
        return plazaAsignada




