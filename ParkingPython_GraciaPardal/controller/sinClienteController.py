import services.clienteService as clienteService
import services.plazaService as plazaService
import services.tipoService as tipoService
import services.ticketService as ticketService
from datetime import date
from datetime import datetime
from models.models import Ticket


def depositarVehiculo():
    matricula = input("Indique la matricula: ")
    for tipo in tipoService.allTipos():
        print(tipo)
    idTipo = int(input("Indique el id del tipo de su vehiculo: "))
    tipo = tipoService.buscarTipoPorId(idTipo)
    plaza = plazaService.asignarPlazaSinCliente(tipo)
    idPlaza = plaza.id
    pin = ticketService.generarPin()
    ticket = Ticket (matricula,datetime.now(),pin,idPlaza)
    ticketService.addTicket(ticket)
    return ticket

def retirarVehiculo():
    matricula = input("Indique la matricula de su vehiculo")
    idPlaza = int(input("Id de la plaza: "))
    pinSocio= int(input("Introdruzca el pin del ticket: "))
    plaza = plazaService.buscarPlazaPorId(idPlaza)
    ticket = ticketService.ticketByPlaza(plaza)
    ticketBis =ticketService.ticketByPin(pinSocio)
    if ticket == ticketBis:
        plazaService.retirarSinCliente(ticket, plaza)
        total = ticketService.calcularTotal(ticket.id)
        ticket.setPrecioFinal = total
        ticketService.editTicket(ticket)
    return ticket


