class vehiculo():
    def __innit__ (self, color,rueda):
        self.color = color
        self.rueda = rueda
    
class Coche (vehiculo):
    def __init__(self, color,rueda,velocidad,cilindrada):  
        vehiculo(). __init__(self,color,rueda)
        self.velocidad= velocidad  
        self.cilindrada= cilindrada
     


