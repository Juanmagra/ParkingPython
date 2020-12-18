import repository.ticketRepository as ticketRepository
import repository.plazaRepository as plazaRepository
import random

def allTickets():
    return ticketRepository.todosTickets()

def ticketById(id):
    return ticketRepository.buscarTicketPorId(id)

def ticketByPin(pin):
    return ticketRepository.buscarTicketPorPin(pin)

def ticketByPlaza(plaza):
    return  ticketRepository.buscarTicketPorPlaza(plaza)

def addTicket(ticket):
    return ticketRepository.añadirTicket(ticket)

def deleteTicket(id):
    return ticketRepository.eliminarTicket(id)

def editTicket(id, ticket):
    return ticketRepository.editarTicket(id , ticket)
def generarPin():
    return random.randint(111111, 999999)

def calcularTotal(id):
    total =0
    ticket = ticketById(id)
    entrada =ticket.fechaEntrada
    salida = ticket.fechaSalida

    diff = salida - entrada

    days, seconds = diff.days, diff.seconds
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    plaza =plazaRepository.buscarPlazaPorId(ticket.plaza.id)

    if seconds >1 :
        minutes +1

    if plaza.tipoPlaza.upper() == "moto":
        total = minutes * 0.08

    if plaza.tipoPlaza.upper()== "turismo":
        total = minutes * 0.12

    if plaza.tipoPlaza.upper() == "minusvalido":
        total = minutes * 0.10


    return total
