class vehiculo():
    def __innit__ (self, color,rueda):
        self.color = color
        self.rueda = rueda
    
class Coche (vehiculo):
    def __init__(self, color,rueda,velocidad,cilindrada):  
        vehiculo(). __init__(self,color,rueda)
        self.velocidad= velocidad  
        self.cilindrada= cilindrada
    def __str__ (self):
        return'coche color{}, numero de ruedas {}, velocidad {} y cilindrada{}'. format(self.color,self.ruedas,self.velocidad,self.cilindrada)
     

class camioneta (Coche):
    def __init__(self, color, rueda, velocidad, cilindrada,carga):
        Coche().__init__(self, color, rueda, velocidad, cilindrada)
        self.carga= carga

    def __str__ (self):
        return'coche color{}, numero de ruedas {}, velocidad {} , cilindrada{} y carga {}'. format(self.color,self.ruedas,self.velocidad,self.cilindrada, self.carga)


class Bicicleta (vehiculo):


