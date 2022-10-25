class vehiculo():
    def __innit__ (self, color,rueda):
        self.color = color
        self.rueda = rueda
    
class Coche (vehiculo):
    def __init__(self, color,rueda,velocidad,cilindrada):  
        vehiculo(). __init__(self,color,rueda)
        self.velocidad= velocidad  
        self.cilindrada= cilindrada
     

class camioneta (Coche):
    def __init__(self, color, rueda, velocidad, cilindrada,carga):
        Coche().__init__(self, color, rueda, velocidad, cilindrada)
        self.carga= carga

    def __str__ (self):
        print('coche color{}, numero de ruedas {}, velocidad {} y cilindrada{}'. format(self.color,self.ruedas,self.velocidad,self.cilindrada))

        


