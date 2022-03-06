def leer(arg1):
    with open(arg1) as archivo:
        lineas = archivo.readlines()
        my_list = []
        for element in lineas:
            element=element.strip("valor=")
            element=element.strip("\n") 
            my_list.append(element)
        return(my_list)

def escribir(arg):
    out = open('file.txt', 'w')
    for element in arg:
        out.writelines("valor="+element+"\n")
    out.close()
