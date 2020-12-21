from datetime import datetime, timedelta

import services.clienteService as clienteService
import services.plazaService as plazaService
import services.ticketService as ticketService
import services.tipoService as tipoService
from models.models import Ticket


def depositarVehiculo():
    matricula = int(input("Matricula del vehiculo: "))
    dni = input("DNI sin letra: ")
    cliente = clienteService.clientePorDni(dni)
    plaza = plazaService.plazaById(cliente.plazaId)
    plaza.setOcupada = True
    plazaService.editarPlaza(plaza)
    tipo = tipoService.buscarTipoPorNombre(plaza.tipoPlaza)
    tipo.setCantidadUsada +=1
    tipoService.editarTipo(tipo)
    ticket = Ticket(matricula,datetime.now(),cliente.abonoPin,plaza.id)
    ticketService.addTicket(ticket)

    return ticket

def retirarVehiculo():
    matricula = int(input("Matricula del vehiculo:"))
    idPlaza = input("Id de la plaza: ")
    pinAbono = input("Pin de abonado: ")
    plaza = plazaService.plazaById(idPlaza)
    plaza.setOcupada = False
    plazaService.editarPlaza(plaza)
    tipo = tipoService.buscarTipoPorNombre(plaza.tipoPlaza)
    tipo.setCantidadUsada-=1
    tipoService.editarTipo(tipo)
    ticket = ticketService.ticketByPlaza(idPlaza)
    ticket.setFechaSalida = datetime.now()
    ticket.setPrecioFinal = "Abonado"
    ticketService.editTicket(ticket)

    return ticket





