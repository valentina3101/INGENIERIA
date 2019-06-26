class Punto(object):

    """ Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas."""
		
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

class Rectangulo(Punto):
	
	def __init__(self, lista, x=0, y=0):
		self.lista = lista 
		Punto().__init__(self, x=0, y=0)
		
	def crear_rect(self, a, b, c, d):
		self.lista 
		
