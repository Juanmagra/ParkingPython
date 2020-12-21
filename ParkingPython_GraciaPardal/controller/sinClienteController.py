from datetime import datetime, timedelta

import services.plazaService as plazaService
import services.ticketService as ticketService
import services.tipoService as tipoService
import services.clienteService as clienteService
from models.models import Ticket, Moto, Turismo, Minusvalido, Vehiculo, Cliente


def depositarVehiculo():
    matricula = input("Indique la matricula: ")
    for tipo in tipoService.allTipos():
        print(tipo)
    idTipo = int(input("Indique el id del tipo de su vehiculo: "))
    tipo = tipoService.buscarTipoPorId(idTipo)
    plaza = plazaService.asignarPlazaSinCliente(tipo)
    idPlaza = plaza.id
    pin = ticketService.generarPin()
    ticket = Ticket(matricula, datetime.now(), pin, idPlaza)
    ticketService.addTicket(ticket)
    # listaOrdenada = sorted(plazaService.allPlazas(), key= lambda x: str(x.id))
    # for i in listaOrdenada:
    #     print(i)
    return ticket


def retirarVehiculo():
    matricula = input("Indique la matricula de su vehiculo: ")
    idPlaza = input("Id de la plazaId: ")
    pinSocio = int(input("Introdruzca el pin del ticket: "))
    plaza = plazaService.plazaById(idPlaza)
    if plaza==False:
        print("Problema encontrando la plazaId")
    else:
        ticket = ticketService.ticketByPlaza(plaza)
        ticketBis = ticketService.ticketByPin(pinSocio)

    if ticket == ticketBis:
        plazaService.retirarSinCliente(ticket, plaza)
    else:
        print("Datos erroneos")

    return ticket


def creaCliente():
    dni = input("Introduzca su DNI sin letra: ")
    nombre = input("Intorduzca su nombre: ")
    matricula = input("Introduzca la matricula de su vehiculo: ")
    vehiculo = None
    fechaAlta = datetime.now()
    fechaExpiracion = None
    plazaAsignada = None
    abonoPin = None

    # Asignar a un sercvicio en clienteService
    tipo = input("Su vehiculo es:\n 1. Moto\n 2. Turismo\n 3. Movilidad Reducida\n ")
    if tipo == "1":
        vehiculo = Moto(matricula)
    elif tipo=="2":
        vehiculo = Turismo(matricula)
    elif tipo =="3":
        vehiculo = Minusvalido(matricula)
    else:
        print("Tipo no valido")

    #Asignar a un servicio en ticketService
    if vehiculo is None:
        print("Ocurrio un error relacionado con el vehiculo.")
    else:
        sub = input("¿Qué tipo de subscripción desea?\n 1. Mensual\n 2. Trimestral\n 3. Semestral\n 4. Anual\n")

        if sub =="1":
            fechaExpiracion = datetime.now() + timedelta(days=30)

        elif sub =="2":
            fechaExpiracion = datetime.now() + timedelta(days=90)

        elif sub == "3":
            fechaExpiracion = datetime.now() + timedelta(days=180)

        elif sub =="4":
            fechaExpiracion = datetime.now() + timedelta(days=365)

        else:
            print("Tipo no valido")

    if fechaExpiracion is None:
        print("Problema relacionado con el abono.")
    else:
        plazaAsignada = plazaService.asignarPlazaCliente(vehiculo)
        abonoPin = ticketService.generarPin()

    if  plazaAsignada is None or abonoPin is None:
        print("Ocurrio un problema con la plazaId o el abonoPin.")
        return False
    else:
        cliente = Cliente(dni,nombre,abonoPin,vehiculo,plazaAsignada.id,fechaAlta,fechaExpiracion)
        clienteService.addCliente(cliente)
        return cliente









