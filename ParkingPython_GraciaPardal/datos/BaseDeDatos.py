import pickle
from datetime import datetime, timedelta

from models.models import *
# Fecha de expiracion (6 meses)
expiracion = datetime.now() + timedelta(days=180)
# Vehiculos
moto = Moto("1111")
minusvalido = Minusvalido("2222")
turismo = Turismo("3333")

# Clientes
cliente1 = Cliente("1111D", "Juan Manuel", 1234, moto, '04', datetime.now(), expiracion)
cliente2 = Cliente("2222D", "Pedro Luis", 4567, turismo, '14', datetime.now(), expiracion)
cliente3 = Cliente("3333D", "Alberto Rodriguez", 7894, minusvalido, '29', datetime.now(), expiracion)
listaDeClientes = [cliente1, cliente2, cliente3]

# Tipo de plazas
tipoMoto = TipoPlaza(1, "MOTO",10)
tipoTurismo = TipoPlaza(2, "TURISMO", 15)
tipoMinusvalido = TipoPlaza(3, "MINUSVALIDO", 5)

listaDeTipos = [tipoMoto, tipoTurismo, tipoMinusvalido]

# Generar todas las plazas del parking
listaDePlazas = [Plaza]

id = 3
for i in listaDeTipos:
    for j in range(i.cantidadDisponible):
        id += 1
        if id-10 < 0:
            id = str(id)
            id =id.zfill(2)

        id = str(id)
        plaza = Plaza(id, i.nombre)
        if id=='04' or id=='14' or id=='29':
            plaza.setReservada=True

        listaDePlazas.append(plaza)
        id = int(id)

for i in listaDeTipos:
    i.setCantidadDisponible-=1
    i.setCantidadReserved+=1


# El ultimo id es 33
for i in listaDePlazas:
    print(i.id, i.tipoPlaza, i.reservada, i.ocupada)


parking = Parking(listaDeClientes, listaDePlazas, listaDeTipos, [], 33)

# # Escritura en modo binario, vacía el fichero si existe
fichero = open('datos.pckl', 'wb')
#
# # Escribe la colección en el fichero
pickle.dump(parking, fichero)
#
fichero.close()
