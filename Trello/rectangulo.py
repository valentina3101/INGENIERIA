
'''
Crear un clase rectangulo que tiene los siguientes atributos:
vertice1
vertice2
vertice3
vertice4

los cuantro vertices son pumtos (x,y)
y metodos 

altura 
base 
superficie 
'''
class Punto(object):

    """ Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas."""
		
    def __init__(self, x=0, y=0, **kw):
        self.x = x
        self.y = y
        super()__init__(**kw)
        
	def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
    #HACER METODO motrar x y mostrar y

class Rectangulo(Punto):
	
	def __init__(self, lista, x=0, y=0):
		self.lista = lista
		super()__init__(lista, x=0, y=0,**kw)
	
	def altura(self):
        area= base * altura
        altura = area/base

    def base(self):
        area = base * altura
        base = area / altura

    def superficie(self):
        superficie=base+altura
		
		
		

		
		
		 
		
	
