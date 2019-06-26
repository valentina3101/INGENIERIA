class Poligono():
    def __init__(self, lista):
        self.lista = lista




'''
6) Crear la clase Rectangulo que tiene los siguientes atributos:
- vertice1
- vertice2
- vertice3
- vertice4
Los cuatro vértices son puntos. Es decir pares (x, y).
Y métodos:
- altura
- base
- superficie
'''
class Rectangulo(Poligono):

    def altura(self):
        area= base * altura
        altura = area/base

    def base(self):
        area = base * altura
        base = area / altura

    def superficie(self):
        superficie=base+altura