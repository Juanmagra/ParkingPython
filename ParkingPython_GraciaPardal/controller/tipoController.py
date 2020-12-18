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
print("\n El tipo 34:")
print((tipoPorId(34)))

print("\n Eliminar tipo vacio:")
deleteTipo(34)

print("\n Todos los tipos:")
for cli in allTipos():
    print(cli)
