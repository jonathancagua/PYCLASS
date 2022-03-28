from operator import truediv

class Inventario:

    def __init__(self):
        try:
            with open('config.txt', 'r') as fd:
                self.__path = fd.read()
        except IOError:
            self.__path=""
            print(" No existe config.txt ")
            # If not exists, create the file
            #print(self.__path)
      
    def load_csv(self):
        my_list = []
        try:
            with open(self.__path,"r",encoding="utf-8") as archivo:
                basura = archivo.readline()
                while(True):
                    linea = archivo.readline()
                    if not linea:
                        break
                    elemento=linea.split(",")
                    #id,nombre,compra,venta
                    my_dic_tmp = {}
                    my_dic_tmp['id']=int(elemento[0])
                    my_dic_tmp['value1']=float(elemento[2])
                    my_dic_tmp['value2']=float(elemento[3].strip("\n"))
                    my_dic_tmp['name']=elemento[1]
                    my_list.append(my_dic_tmp)
                return my_list
        except IOError:
            print(" No existe config.txt ")
            return my_list
