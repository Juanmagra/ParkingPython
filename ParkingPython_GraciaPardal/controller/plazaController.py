from services.plazaService import *

print("\n Todas las plazas:")
for cli in allPlazas():
    print(cli)
print("\n La plaza con id 14:")
print((plazaById(14)))

print("\n Añadir plaza:")
plaza = Plaza()
addPlaza(plaza)
for cli in allPlazas():
    print(cli)


print("\n Eliminar plaza con id 25:")
deletePlaza(25)

print("\n Todas las plazas:")
for cli in allPlazas():
    print(cli)


