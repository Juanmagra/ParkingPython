import random

import repository.plazaRepository as plazaRepository
import repository.ticketRepository as ticketRepository


def allTickets():
    return ticketRepository.todosTickets()


def ticketById(id):
    return ticketRepository.buscarTicketPorId(id)


def ticketByPin(pin):
    return ticketRepository.buscarTicketPorPin(pin)


def ticketByPlaza(plaza):
    return ticketRepository.buscarTicketPorPlaza(plaza)


def addTicket(ticket):
    return ticketRepository.añadirTicket(ticket)


def deleteTicket(id):
    return ticketRepository.eliminarTicket(id)


def editTicket(ticket):
    return ticketRepository.editarTicket(ticket)


def generarPin():
    return random.randint(111111, 999999)


def calcularTotal(ticket):
    total = 0
    entrada = ticket.fechaEntrada
    salida = ticket.fechaSalida

    diff = salida - entrada

    days, seconds = diff.days, diff.seconds
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    plaza = plazaRepository.buscarPlazaPorId(ticket.plazaId)
    if seconds > 1:
        minutes += 1

    if plaza.tipoPlaza == "MOTO":
        total = minutes * 0.08
        if total == 0.0:
            total = 0.08

    if plaza.tipoPlaza == "TURISMO":
        total = minutes * 0.12
        if total == 0.0:
            total = 0.12

    if plaza.tipoPlaza == "MINUSVALIDO":
        total = minutes * 0.10
        if total == 0.0:
            total = 0.10

    return total
