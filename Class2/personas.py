from operator import truediv


class Persona:
    def __init__(self,nombre,edad):
        self.set_nombre(nombre)
        self.set_edad(edad)

    def set_edad(self,edad):
        if 0 <= edad <= 125:
            self.__edad= edad

    def get_edad(self):
        return self.__edad

    def set_nombre(self,nombre):
        if nombre!="":
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def print_persona(self):
        print("{} {}".format(self.get_nombre(),self.get_edad()))

    def es_mayor_de_edad(self):
        if(self.get_edad() >= 18):
            return True
        else:
            return False

    def es_mayor_que(self , otra_persona):
        if(self.get_edad() > otra_persona.get_edad()):
            return True
        else:
            return False
    @staticmethod 
    def get_mayor(persona_1 , persona_2):
        if(persona_1.get_edad() > persona_2.get_edad()):
            return persona_1
        else:
            return persona_2
    @staticmethod        
    def dump_csv(file_name,lista):
        with open(file_name,"w",encoding="utf-8") as f:
            f.write("Nombre,edad\n")
            for per in lista:
                linea = f"{per.get_nombre()},{per.get_edad()}\n"
                #linea = "{},{}".format(per.get_nombre(),per.get_edad())
                #linea = per.get_nombre()+","+str(per.get_edad())
                f.write(linea)
    @staticmethod        
    def load_csv(file_name):
        my_list = []
        with open(file_name,"r",encoding="utf-8") as archivo:
            basura = archivo.readline()
            while(True):
                linea = archivo.readline()
                if not linea:
                    break
                elemento=linea.split(",")
                my_list.append(Persona(elemento[0],int(elemento[1])))
            return my_list
