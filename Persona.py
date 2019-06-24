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
        print(self.nombre + " " + self.apellido + " " + (str(self.dni)) + " " + (str(self.edad)))
        
        
    def habla(self, dice):
        print(dice)


class Docente(Persona):  
      "clase que representa a un Docente (hereda de persona)"
      def __init__(self, nombre,apellido,dni,edad,materia,num_legajo,cant_alumn_a_cargo,años_antigüedad,**kw):
        self.materia = materia
        self.num_legajo = num_legajo
        self.cant_alumn_a_cargo = cant_alumn_a_cargo
        self.años_antigüedad = años_antigüedad
        super().__init__(nombre=nombre,apellido=apellido,dni=dni,edad=edad,**kw)
        
      
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
    
        
class Docente_teorico(Docente):
    
    def __init__(self):
        super().__init()
        
        
    def Dar_teorico(unidad):
        pass
        
    def Proponer_examen(self,materia):
        if materia == Geografia:
            print("Cual es el rio más ancho del mundo")
        if materia == Matematica:
            print("Cuantos lados tiene un poligono")
        if materia == Programacion:
            print("Que es scrum")      
        
        
class Docente_practico(Docente):
    def __init__(self):
        super(Docente,self).__init__()
    
    def Dar_practico():   
        if materia == Matematica:
            print("ejer auto")
        if materia == Programacion:
            print("ej python")
            
if __name__=="__main__":
    a=Persona("Juan","Perez",23456789,34)
    a.__str__()
    a.habla("Hola alumnos")            
    b=Docente("Maria","Lopez",98765432,54,"Geografia",67,30,8) 
    b.__str__()            
    b.Proponer_examen("Programacion")
                   

            
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
        print("Estoy dando la clase de" + self.materia + self.cant_alumn)
        
'''
#Docente tiene los siguientes atributos
#- Materia. Puede ser: Geografía, Matemática, Programación
#- Numero de legajo
#- Cantidad de alumnos a cargo
#- Años de antigüedad
#Y métodos:
#- corregir. Que dada una lista de 2-uplas (respuesta_correcta, respuesta_del_alumno), 
 imprime el porcentaje de respuestas correctas del alumno.
#- Dar clases. Que dado un string con el nombre de la unidad, imprime por pantalla 
“Estoy dando la clase de [unidad] a mis [cantidad de alumnos]
'''
'''DocenteTeorico no tiene atributos especificos
Y métodos:
- Dar teórico. Que dada una unidad, da clase de esa unidad
- Proponer examen. Que, si es profesor de:
* Geografia: pregunta “Cuál es el rio más ancho del mundo? 1) De la plata, 2) Nylo, 3)
Amazonas”
*Matemática: pregunta “Cuántos lados tiene un polígono? 1) 5, 2) más de 2, 3) 5 o más”
*Programación: pregunta “Qué es Scrum? 1) Una forma de escribir código, 2) Una
metodología ágil, 3) Una herramienta de debugging”
DocentePractico sólo puede ser docente de Matemática o Programación y no tiene atributos extras
Y métodos:
- Dar practico. Que dada una unidad, da la clase de esa unidad y propone (imprimiendo por
pantalla) alguno de los siguientes ejercicios:
*Si es de Matemática: “Cuánta plata gastaste si hiciste 10km en un auto que consume 1.5
litros por cada kilómetro y la nafta cuesta 50 pesos por litro? 1) 800, 2) 750, 3) 500”
*Si es de Programación: “En Python, qué valor resulta de hacer ‘a == b == a is b’ si tanto a
como b tienen en valor [1, 2, 3]? 1) True, 2) False, 3) Da error”
'''
