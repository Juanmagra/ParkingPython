import controller.conClienteController as conClienteController
import controller.sinClienteController as sinClienteController
app = True
while app:
    user = input("Bienvenido a ParkingPython\n 1. Usuario\n 2. Administrador\n 0. Cerrar\n Entrada:  ")
    #Usuario
    if user == "1":
        opcion = input("\n 1. Crear cliente\n 2. Depositar con cliente\n 3. Depositar sin cliente\n 4. Retirar con cliente\n 5. Retirar sin cliente\n Entrada: ")
        if opcion =="1":
            cliente = sinClienteController.creaCliente()
            if cliente ==False:
                print("Ocurrio un problema creano0"
                      " el cliente.")
            else:
                print("Cliente creado con exito!\n")
                print(cliente)

        elif opcion =="2":
            ticket = conClienteController.depositarVehiculo()
            if ticket == False:
                print("Ocurrio un problema generando el Ticket.")
            else:
                print("Deposito con exito.")
                print(ticket)

        elif opcion == "3":
            ticket = sinClienteController.depositarVehiculo()
            if ticket ==False:
                print("Ocurrio un problema generando el Ticket.")
            else:
                print("Deposito con exito.")
                print(ticket)

        elif opcion == "4":
            ticket = conClienteController.retirarVehiculo()
            if ticket ==False:
                print("Ocurrio un problema al retirar el vehiculo.")
            else:
                print("Retirada con exito.")
                print(ticket)

        elif opcion == "5":
            ticket = sinClienteController.retirarVehiculo()
            if ticket ==False:
                print("Ocurrio un problema al retirar el vehiculo.")
            else:
                print("Retirada con exito.")
                print(ticket)
        else:
            print("Opcion no valida.")

    #Admin
    elif user =="2":
        print("ADMIN")
    #Cerrar
    else:
        print("Cerrando el programa, vuelva pronto.")
        app = False


