from services.tipoService import *

print("\n Todos los Tipos:")
for cli in allTipos():
    print(cli)
print("\n El tipo moto:")
print((tipoPorNombre("moto")))

print("\n Añadir tipo vacio:")
tipo = TipoPlaza()
addTipo(tipo)
for cli in allTipos():
    print(cli)
print("\n El tipo 0:")
print((tipoPorId(0)))

print("\n Eliminar tipo vacio:")
deleteTipo(0)

print("\n Todos los tipos:")
for cli in allTipos():
    print(cli)
