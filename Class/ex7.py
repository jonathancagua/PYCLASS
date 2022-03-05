with open('file.txt') as archivo:
    lineas = archivo.readlines()
    my_list = []
    for element in lineas:
        element=element.strip("valor=")
        element=element.strip("\n") 
        my_list.append(element)
    print(my_list)