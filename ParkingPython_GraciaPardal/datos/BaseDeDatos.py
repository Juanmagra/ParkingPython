import pickle
from models.models import *
from datetime import date
from datetime import datetime, timedelta

#Fecha de expiracion (6 meses)
expiracion = datetime.now()+ timedelta(days=180)

#Vehiculos
moto = Moto("MattriculaMotoJuan")
minusvalido = Minusvalido ("MatriculaMinus")
turismo = Turismo("MatriculaTursimo")

#Clientes
cliente1 =  Cliente("1111D","Juan Manuel",1234,moto,4,datetime.now(),expiracion)
cliente2 = Cliente("2222D", "Pedro Luis", 4567,turismo,14,datetime.now(),expiracion)
cliente3 =  Cliente("3333D","Alberto Rodriguez",7894,minusvalido,29,datetime.now(),expiracion)
listaDeClientes = [cliente1,cliente2,cliente3]

#Tipo de plazas
tipoMoto = TipoPlaza(1,"MOTO",10)
tipoMinusvalido = TipoPlaza(2, "MINUSVALIDO",5)
tipoTurismo = TipoPlaza(3,"TURISMO",15)
listaDeTipos = [tipoMoto,tipoTurismo,tipoMinusvalido]

#Generar todas las plazas del parking
listaDePlazas = [Plaza]

id=3
for i in listaDeTipos:
    for j in range(i.cantidadDisponible):
        id+=1
        plaza = Plaza(id,i.nombre)
        listaDePlazas.append(plaza)
#El ultimo id es 33
for i in listaDePlazas:
    print(i.id, i.tipoPlaza, i.reservada, i.ocupada)

parking = Parking(listaDeClientes,listaDePlazas,listaDeTipos, [],33)

# # Escritura en modo binario, vacía el fichero si existe
fichero = open('datos.pckl','wb')
#
# # Escribe la colección en el fichero
pickle.dump(parking, fichero)
#
fichero.close()