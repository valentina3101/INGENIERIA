#4) Escribir las clases:
#Perro que inicie en la posición cero y que tenga los siguiente métodos:
#- caminar. Que cambie la posición 4 lugares posterior.
#- ladrar. Que imprima por pantalla “Guau Guau”
#Gato que inicie en la posición cero y que tenga los siguientes métodos:
#- trepar. Que imprima por pantalla “Estoy arriba del arbol”
#- caminar. Que cambie la posición 10 lugares posterior.
#- maullar. Que imrima por pantalla “Miau”
#Una función que se llame pasear_mascota que tome una mascota y que la haga caminar cinco
#veces y que luego de eso imprima por pantalla “La mascota quedó en [posicion donde quedo la
#mascota]" 


def pasear_mascota(mascota):
    for i in range(5):
        mascota.caminar()

    print ("la mascota quedo:" + (str(mascota.posicion)))
    

class Mascota():
    def __init__(self,posicion):
        self.posicion = 0
        super().__init__()
    
    def caminar(posicion):
        pass 


class Perro(Mascota):
    def __init__(self,**kw): #toma posicion
        super().__init__(posicion=posicion)

    def caminar(self,posicion): #toma posicion de mascota
        self.posicion += 4
        print (self.posicion)
   
    def __str__():
        print ("Guau Guau") 

class Gato(Mascota):
    def __init__ (self,**kw): #posicion de mascota
        super().__init__(**kw) #posicion
        
    def trepar():
        print ("estoy arriba del arbol")    
   
    def caminar(posicion): #toma posicion de mascota
        self.posicion += 10
        print (self.posicion)

    def __str__():
        print ("Miau")

if __name__ == "__main__":
    a = Perro
    a.__str__()
    b= Gato
    b.trepar()
    b.__str__()
    a.pasear_mascota()


