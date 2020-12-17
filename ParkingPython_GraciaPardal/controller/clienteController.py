from services.clienteService import *

print("\n Todos los clientes:")
for cli in allClientes():
    print(cli)
print("\n El cliente 2222D:")
print((clientePorDni("2222D")))

print("\n Añadir cliente vacio:")
cliente = Cliente()
addCliente(cliente)
for cli in allClientes():
    print(cli)
print("\n El cliente 0:")
print((clientePorDni(0)))

print("\n Eliminar cliente vacio:")
deleteCliente(0)

print("\n Todos los clientes:")
for cli in allClientes():
    print(cli)


