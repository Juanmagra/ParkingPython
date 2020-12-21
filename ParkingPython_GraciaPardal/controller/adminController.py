import services.plazaService as plazaService
import  services.clienteService as clienteService
import services.ticketService as ticketService
def listarPlazas():
    plazas = plazaService.allPlazas()
    print("|    ID  |   Reservada   |   Ocupada |   Tipo    |")
    for plaza in sorted(plazas, key=lambda plaza : str(plaza.id)):
        print("|    %s  |   %s        |   %s    |   %s  |"%(plaza.id, plaza.reservada, plaza.ocupada, plaza.tipoPlaza))

def listarAbonados():
    clientes = clienteService.allClientes()
    for cliente in sorted(clientes, key=lambda cliente : str(cliente.plazaId)):
        print("La lista de clientes es:")
        print(cliente)

def listarTickets():
    tickets = ticketService.allTickets()
    for ticket in sorted(tickets, key=lambda ticket : str(ticket.id)):
        print("Lista de ticktes: ")
        print(ticket)

# def listarTickets(fecha1, fecha2):
#     tickets = ticketService.allTickets()
#     listaDeseada = [Ticket]
#     for ticket in tickets:
#         if ticket.fechaSalida in (fecha1,fecha2):
#             listaDeseada.append(ticket)
#
#     for ticket in listaDeseada:
#         print("Lista de ticktes: ")
#         print(ticket)