from personas import Persona

#lista = []
"""p1= Persona("jon",39)
p2 = Persona("Clara",35)
p3= Persona("jonathan",15)
p4 = Persona("Amalia",25)

lista.append(p1)
lista.append(p2)
lista.append(p3)
lista.append(p4)

for per in lista:
    if per.es_mayor_de_edad():
        per.print_persona()
"""

lista = Persona.load_csv("personas.csv")

for per in lista:
    per.print_persona()