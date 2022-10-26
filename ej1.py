

#Apartado 1 creamos las clases
class vehiculo():
    def __innit__ (self, color,rueda):
        self.color = color
        self.ruedas = ruedas
    
class Coche (vehiculo):
    def __init__(self, color,rueda,velocidad,cilindrada):  
        vehiculo(). __init__(self,color,rueda)
        self.velocidad= velocidad  
        self.cilindrada= cilindrada
    def __str__ (self):
        return'coche color{}, numero de ruedas {}, velocidad {} y cilindrada{}'. format(self.color,self.ruedas,self.velocidad,self.cilindrada)
     

class camioneta (Coche):
    def __init__(self, color, rueda, velocidad, cilindrada,carga):
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
