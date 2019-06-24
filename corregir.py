def corregir(self, respuesta):
    
    for elemento in respuesta:
        respuesta_correcta = respuesta[0]
        respuesta_alumno = respuesta[1]
        if respuesta_correcta[0] == respuesta_alumno[1]:
            print("respuestas correctas del alumno")
        else:
            print("respuestas incorrecta")
         
##resp = [(2 ,3), (6, 1), (6, 6)]
##pregunta = (2, 3)
##pregunta[0] 
    
##corregir. Que dada una lista de 2-uplas (respuesta_correcta, respuesta_del_alumno), 
##imprime el porcentaje de respuestas correctas del alumno.

