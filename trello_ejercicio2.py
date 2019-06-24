#Reescribir las clases Repartidor y Comercial, utilizando la clase padre Empleado.
#Diseñar e implementar dicha clase y las dos hijas

class Empleado(object):
    def __init__(self,nombre,apellido,edad,salario,**kw):
        self.nombre= nombre
        self.apellido= apellido
        self.edad = edad
        self.salario=salario
        super().__init__(**kw)

    def __str__ (self):
        print (self.nombre + " " + self.apellido)


class Comercial(Empleado):
    def __init__(self,nombre,apellido,edad,salario,comision,**kw): 
        super().__init__(nombre=nombre,apellido=apellido,edad=edad,salario=salario,**kw)
        self.comision=comision
    
    def plus (self,porcentaje):
        if self.edad > 30 and self.comision > 200:
            print ("recibio plus")
        
        aumento= self.salario * porcentaje
        self.salario += porcentaje

class Repartidor(Empleado): #Crea una clase Repartidor
    def __init__(self,nombre,apellido,edad,salario,zona,**kw):
        self.zona=zona
        super().__init__(nombre=nombre,apellido=apellido,edad=edad,salario=salario,**kw)

    def plus(self, x):
        if x <= 1:
            aumento= self.salario * x

        if self.edad < 25 and self.zona == 3: 
            print ("recibio el plus")
            self.salario += aumento

if __name__ == "__main__":
    a = Empleado ("juana","juarez",36 , 15000)
    a.__str__() 
    c= Comercial('mauro','cisneros',31,14000,300)
    c.__str__()
    c.plus(1)
    b = Repartidor('juan','perez',30,13000,3)
    b.__str__()

    
