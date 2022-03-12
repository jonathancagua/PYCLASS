from personas import Persona

p= Persona("jon",39)
p2 = Persona("Clara",55)
presp = p.get_mayor(p,p2)
print("Es mayor:")
presp.print_persona()

