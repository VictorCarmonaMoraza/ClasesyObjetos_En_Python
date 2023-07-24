
# Creacion de una clase
class Persona:
    #Metodo inicializador
    def __init__(self, nombre, apellido, edad):
        #Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


#Creacion de un objeto de esta clase
persona1 = Persona('Juan','Carmona',28)

#Imprimimos valores de la instancia persona1
print(f'Objeto numero 1 {persona1.nombre} {persona1.apellido} {persona1.edad}')

#Creacion de un segundo objeto de tipo Persona
persona2 = Persona('Karla','Gomez',45)

#Imprimimos valores de la instancia persona2
print(f'Objeto numero 2 {persona2.nombre} {persona2.apellido} {persona2.edad}')
