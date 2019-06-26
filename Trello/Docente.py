class Persona(object):   
    "esta clase representa a una Persona"

    def __init__(self, nombre, apellido, dni, edad, **kw): 
        "constructor de Persona"
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.edad = edad
        super().__init__(**kw)
        
    def __str__(self):
        print(self.nombre +" "+ self.apellido +" " + (str(self.dni)) + " " + (str(self.edad)))
          
    def habla(self,string):
        print (string)



class Docente(Persona):  
      "clase que representa a un Docente (hereda de persona)"

    def __init__(self, nombre,apellido, dni, edad, materia, num_legajo, cant_alumn_a_cargo, años_antigüedad, **kw):
        self.materia = materia
        self.num_legajo = num_legajo
        self.cant_alumn_a_cargo = cant_alumn_a_cargo
        self.años_antiguedad = años_antiguedad
        super().__init__(nombre=nombre,apellido=apellido,dni=dni,edad=edad,**kw)

     def __str__(self):
        print (self.materia + (str(self.num_legajo)), (str(cant_alumn_a_cargo)) + (str(años_antiguedad)))
      
    def corregir(self, respuesta):
		
        for respuesta in respuesta:
        respuesta_correcta = respuesta[0]
        respuesta_alumno = respuesta[1]
            if respuesta_correcta[0] == respuesta_alumno[1]:
                print("respuestas correctas del alumno")
            else:
                print("respuestas incorrecta")
                print("respuestas correctas del alumno")
            else:
            
    def Dar_clases(self):
        nombre_de_unidad = str()
        print("Estoy dando la clase de" + self.materia + self.cant_alumn)
        
    
        
class Docente_teorico(Persona, Docente):
    
    def __init__(self):
        pass
        
    def Dar_teorico(unidad):
        
    def Proponer_examen(materia):
        if materia == Geografia:
            print("Cual es el rio más ancho del mundo")
        if materia == Matematica:
            print("Cuantos lados tiene un poligono")
        if materia == Programacion:
            print("Que es scrum")      
        
        
class Docente_practico(Persona, Docente):        
    def Dar_practico():   
        if materia == Matematica:
            print("ejer auto")
        if materia == Programacion:
            print("ej python")'''
            
if __name__=="__main__":
    a=Persona("Juan","Perez", 23456789, 34)
    a.__str__()
    a.habla('holaa')
    b= Docente("maria","perez",34567890,56,'geografia',34,4,8)
    b.__str__()
                
                 
        
                   

        
'''     
##resp = [(2 ,3), (6, 1), (6, 6)]
##pregunta = (2, 3)
##pregunta[0]

    def corregir(self, resp):
        for respuestas in resp:
            respuesta_correcta = respuesta[0]
            respuesta_alumno = respuesta[1]
            if respuesta[0] == respuesta[1]:
                print("respuestas correctas del alumno")
            else:
                respuesta[0] != respuesta[1]
        print("%respuestas correctas del alumno")
    
    def dar_clases(self):
        nombre_de_unidad = str()
        print("Estoy dando la clase de" + self.materia + self.cant_alumn)'''
        

