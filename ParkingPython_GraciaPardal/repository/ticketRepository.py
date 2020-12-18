import pickle

from models.models import Parking, TipoPlaza, Cliente, Ticket

fichero = open('../datos/datos.pckl', 'rb')

# Cargamos los datos del fichero
lista_fichero = pickle.load(fichero)
parking = lista_fichero
fichero.close()
tickets = parking.listaTicktes

def todosTickets():
    return parking.listaTicktes
def buscarTicketPorId(id):
    ticketId = Ticket()
    for ticket in tickets:
        if ticket.id == id:
            ticketId = ticket
    return ticketId

def buscarTicketPorPin(pin):
    ticketPin = Ticket()
    for ticket in tickets:
        if ticket.pin == pin:
            ticketPin = ticket
    return ticketPin

def buscarTicketPorPlaza(plaza):
    ticketPlaza = Ticket()
    for ticket in tickets:
        if ticket.plaza == plaza:
            ticketPlaza = ticket
    return ticketPlaza

def añadirTicket(ticket):
    if ticket.id == 0:
        ticket.setId = parking.idGenerator()

    tickets.append(ticket)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()

def eliminarTicket(id):
    ticketDel = buscarTicketPorId(id)
    tickets.remove(ticketDel)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()

def editarTicket(id, ticket):
    eliminarTicket(buscarTicketPorId(id))
    ticket.setId = id
    añadirTicket(ticket)
    fichero = open('../datos/datos.pckl', 'wb')
    #
    # # Escribe la colección en el fichero
    pickle.dump(parking, fichero)
    #
    fichero.close()


