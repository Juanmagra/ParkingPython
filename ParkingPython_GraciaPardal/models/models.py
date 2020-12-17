# Class cliente
class Cliente():
    def __init__(self, dni=0, nombre="", abonoPin=0, vehiculo=0, plaza=0, fechaAlta=0, fechaExpiracion=0):
        self.__dni = dni
        self.__nombre = nombre
        self.__abonoPin = abonoPin
        self.__vehiculo = vehiculo
        self.__plaza = plaza
        self.__fechaAlta = fechaAlta
        self.__fechaExpiracion = fechaExpiracion

    # Getters & setters
    @property
    def dni(self):
        return self.__dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def abonoPin(self):
        return self.__abonoPin

    @property
    def vehiculo(self):
        return self.__vehiculo

    @property
    def plaza(self):
        return self.__plaza

    @property
    def fechaAlta(self):
        return self.__fechaAlta

    @property
    def fechaExpiracion(self):
        return self.__fechaExpiracion

    @dni.setter
    def setDni(self, nuevo):
        self.__dni = nuevo

    @nombre.setter
    def setNombre(self, nuevo):
        self.__nombre = nuevo

    @abonoPin.setter
    def setAbonoPin(self, nuevo):
        self.__abonoPin = nuevo

    @vehiculo.setter
    def setVehiculo(self, nuevo):
        self.__vehiculo = nuevo

    @plaza.setter
    def setPlaza(self, nuevo):
        self.__plaza = nuevo

    @fechaAlta.setter
    def setFechaAlta(self, nuevo):
        self.__fechaAlta = nuevo

    @fechaExpiracion.setter
    def setFechaExpiracion(self, nuevo):
        self.__fechaExpiracion = nuevo

    def __str__(self):
        return "dni: %s, nombre: %s, plaza: %s, vehiculo: %s, abonoPin: %s, fechaAlta: %s, fechaExpiracion: %s" % (self.__dni,self.__nombre,self.__plaza,self.__vehiculo, self.__abonoPin, self.__fechaAlta, self.__fechaExpiracion)

    pass


# Final clase cliente

# Clase Tipo Plaza
class TipoPlaza():
    def __init__(self, id=0, nombre="", cantidadDisponible=0, cantidadReserved=0, cantidadUsada=0):
        self.__id = id
        self.__nombre = nombre
        self.__cantidadDisponible = cantidadDisponible
        self.__cantidadReserved = cantidadReserved
        self.__cantidadUsada = cantidadUsada

    # Getters & Setters
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def cantidadDisponible(self):
        return self.__cantidadDisponible

    @property
    def cantidadReserved(self):
        return self.__cantidadReserved

    @property
    def cantidadUsada(self):
        return self.__cantidadUsada

    @id.setter
    def setId(self, nuevo):
        self.__id = nuevo

    @nombre.setter
    def setNombre(self, nuevo):
        self.__nombre = nuevo

    @cantidadDisponible.setter
    def setCantidadDisponible(self, nuevo):
        self.__cantidadDisponible = nuevo

    @cantidadReserved.setter
    def setCantidadReservada(self, nuevo):
        self.__cantidadReserved = nuevo

    @cantidadUsada.setter
    def setCantidadUsada(self, nuevo):
        self.__cantidadUsada = nuevo

    def __str__(self):
        return "id: %s, nombre: %s, cantidadReserved: %s, cantidadUsada: %s, cantidadDisponible %s"%(self.__id,self.__nombre,self.__cantidadReserved, self.__cantidadUsada, self.__cantidadDisponible)

    pass


# Fin clase Tipo Plaza

# Clase Plaza
class Plaza():
    def __init__(self,  id=0, tipoPlaza="", ocupada=False, reservada=False):
        self.__id = id
        self.__tipoPlaza = tipoPlaza
        self.__ocupada = ocupada
        self.__reservada = reservada

    # Getters & Setters
    @property
    def id(self):
        return self.__id

    @property
    def tipoPlaza(self):
        return self.__tipoPlaza

    @property
    def ocupada(self):
        return self.__ocupada

    @property
    def reservada(self):
        return self.__reservada

    @id.setter
    def setId(self, nuevo):
        self.__id = nuevo

    @tipoPlaza.setter
    def setTipoPlaza(self, nuevo):
        self.__tipoPlaza = nuevo

    @ocupada.setter
    def setOcupada(self, nuevo):
        self.__ocupada = nuevo

    @reservada.setter
    def setReservada(self, nuevo):
        self.__reservada = nuevo

    def __str__(self):
        return "id: %s, ocupada: %s, tipoPlaza: %s, reservada: %s "%(self.__id, self.__ocupada, self.__tipoPlaza, self.__reservada)

    pass


# Fin clase Plaza

# Clase Ticket
class Ticket():
    def __init__(self, matricula, fechaEntrada, pin, plaza, precioFinal=0, fechaSalida=0, id=0):
        self.__id = id
        self.__matricula = matricula
        self.__fechaEntrada = fechaEntrada
        self.__pin = pin
        self.__plaza = plaza
        self.__precioFinal = precioFinal
        self.__fechaSalida = fechaSalida

    # Getters & Setters
    @property
    def id(self):
        return self.__id

    @property
    def matricula(self):
        return self.__matricula

    @property
    def fechaEntrada(self):
        return self.__fechaEntrada

    @property
    def pin(self):
        return self.__pin

    @property
    def plaza(self):
        return self.__plaza

    @property
    def precioFinal(self):
        return self.__precioFinal

    @property
    def fechaSalida(self):
        return self.__fechaSalida

    @id.setter
    def setId(self, nuevo):
        self.__id = nuevo

    @matricula.setter
    def setMatricula(self, nuevo):
        self.__matricula = nuevo

    @fechaEntrada.setter
    def setFechaEntrada(self, nuevo):
        self.__fechaEntrada = nuevo

    @pin.setter
    def setPin(self, nuevo):
        self.__pin = nuevo

    @plaza.setter
    def setPlaza(self, nuevo):
        self.__plaza = nuevo

    @precioFinal.setter
    def setPrecioFinal(self, nuevo):
        self.__precioFinal = nuevo

    @fechaSalida.setter
    def setFechaSalida(self, nuevo):
        self.__fechaSalida = nuevo

    def __str__(self):
        return "--------Ticket--------" \
               "* PIN: %s; PLAZA: %s *" \
               "* MATRICULA %s *" \
               "* ENTRADA: %s *" \
               "* SALIDA: %s *" \
               "* PRECIO: %s *" \
               "---GRACIAS POR VENIR---"%(self.__pin, self.__plaza, self.__matricula, self.__fechaEntrada, self.__fechaSalida, self.__precioFinal)
    pass


# Fin clase Ticket

# Clase Parking
class Parking():
    def __init__(self, listaUsuarios=[], listaPlazas=[], listaTipos=[],listaTickets=[], id=0):
        self.__listaUsuarios = listaUsuarios
        self.__listaPlazas = listaPlazas
        self.__listaTickets = listaTickets
        self.__listaTipos = listaTipos
        self.__id = id

    # Getters & Setters
    @property
    def listaUsuarios(self):
        return self.__listaUsuarios

    @property
    def listaPlazas(self):
        return self.__listaPlazas

    @property
    def listaTipos(self):
        return self.__listaTipos

    @property
    def listaTicktes(self):
        return self.__listaTickets
    @property
    def id(self):
        return self.__id

    @listaUsuarios.setter
    def setListaUsuarios(self, nuevo):
        self.__listaUsuarios = nuevo

    @listaPlazas.setter
    def setListaPlazas(self, nuevo):
        self.__listaPlazas = nuevo

    @listaTicktes.setter
    def setListaTickets(self,nuevo):
        self.__listaTickets = nuevo

    @listaTipos.setter
    def setListaTipos(self,nuevo):
        self.__listaTipos = nuevo

    @id.setter
    def id(self, nuevo:int):
        self.__id = nuevo

    def idGenerator(self):
        self.__id +=1
        return self.__id

    pass


# Fin clase Parking

# Clase Vehiculo
class Vehiculo():
    def __init__(self, matricula):
        self.__matricula = matricula

    # Getters & Setters
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def setMatricula(self, nuevo):
        self.__matricula = nuevo

    def __str__(self):
        return "matricula : %s"%(self.__matricula)
    pass


# Clases hijas de vehiculo
class Turismo(Vehiculo):
    def __init__(self, matricula, tarifa=0.12):
        super().__init__(matricula)
        self.__tarifa = tarifa

    # Getters & Setters
    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def setTarifa(self, nuevo):
        self.__tarifa = nuevo

    def __str__(self):
        return super().__str__() + ", tarifa: %s"%(self.__tarifa)

    pass

class Moto(Vehiculo):
    def __init__(self, matricula, tarifa=0.08):
        super().__init__(matricula)
        self.__tarifa = tarifa

    # Getters & Setters
    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def setTarifa(self, nuevo):
        self.__tarifa = nuevo

    def __str__(self):
        return super().__str__() + ", tarifa: %s"%(self.__tarifa)
    pass

class Minusvalido(Vehiculo):
    def __init__(self, matricula, tarifa=0.10):
        super().__init__(matricula)
        self.__tarifa = tarifa

    # Getters & Setters
    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def setTarifa(self, nuevo):
        self.__tarifa = nuevo

    def __str__(self):
        return super().__str__() + ",  tarifa: %s"%(self.__tarifa)

    pass