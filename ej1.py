

#Apartado 1 creamos las clases
class vehiculo():
    def __innit__ (self, color,ruedas):
        self.color = color
        self.ruedas = ruedas
    
class Coche (vehiculo):
    def __init__(self, color,ruedas,velocidad,cilindrada):  
        vehiculo().__init__(self,color,ruedas)
        self.velocidad= velocidad  
        self.cilindrada= cilindrada
    def __str__ (self):
        return'coche color{}, numero de ruedas {}, velocidad {} y cilindrada{}'. format(self.color,self.ruedas,self.velocidad,self.cilindrada)
     

class camioneta (Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        Coche().__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga= carga

    def __str__ (self):
        return'coche color{}, numero de ruedas {}, velocidad {} , cilindrada{} y carga {}'. format(self.color,self.ruedas,self.velocidad,self.cilindrada, self.carga)


class Bicicleta (vehiculo):
    def __init__ (self,color,ruedas,tipo):
        vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return 'Bicicleta tipo {} color {} ruedas {}'.format(self.tipo, self.color,self.ruedas)


class Motocicleta (Bicicleta):
    def __init__(self, color,ruedas,tipo,velocidad,cilindrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad=velocidad
        self.cilindrada = cilindrada

    def __str__ (self):
        return 'Moto tipo {} color {} ruedas {} velocidad {} cilindrada {}'.format(self.tipo, self.color, self.ruedas, self.velocidad, self.cilindrada)

#Apartado 2 creamos función catalogar para identificr el tipo de vehículo 
def catalogar (lista_vehiculos):
    for vehiculo in lista_vehiculos:
        print ('Vehiculo es del tipo {}'.format(type(vehiculo).__name__))
        print (vehiculo)


#Apartado 3 funcion catalogar segunda versión 
def catalogar2 (lista_vehiculos, num_ruedas = None) :
    contador =0
    if num_ruedas != None:
        for vehiculo in lista_vehiculos:
            if vehiculo.ruedas == num_ruedas:
                contador = contador + 1
                print ('Vehiculo es del tipo {}'.format(type(vehiculo).__name__))
                print (vehiculo)

        print ('se ha encontrado {} vehiculos con {} ruedas'.format (contador, num_ruedas))


    else:
     print ('Por favor ingresa un número de ruedas ')



#ejemplos y lista para añadir

vehiculos = []

vehiculo1 = Coche ('Negro', 4, 500, 250)
vehiculo2 = Bicicleta ('gris', 2, 'urbana')
vehiculo3 = camioneta ('Dorada', 4, 150, 120, 500)
vehiculo4 = Motocicleta ('amarilla', 2, 'deportiva', 200, 150)

vehiculos.append(vehiculo1)
vehiculos.append(vehiculo2)
vehiculos.append(vehiculo3)
vehiculos.append(vehiculo4)

catalogar2 (vehiculos, num_ruedas=2)