
class Punto(object):

    """ Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas."""
		
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
		
    def restar(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)
	
    def norma(self):
        return (self.x*self.x + self.y*self.y)**0.5
	
    def distancia(self, otro):
        r = self.restar(otro)
        return r.norma()
	
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Punto(self.x - otro.x, self.y - otro.y)
	
    def __eq (self, otro):
        return self.x == otro.x and self.y == otro.y

    def __ne__(self, otro):
        return not self == otro
        
class Rectangulo(Punto):
	
	def __init__(self, lista, x=0, y=0):
		self.lista = lista 
		Punto().__init__(self, x=0, y=0)
		
	
		
	
	
	
	
	
