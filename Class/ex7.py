def leer(arg1):
    with open(arg1) as archivo:
        lineas = archivo.readlines()
        my_list = []
        dic =  {}
        for element in lineas:
            my_list=element.split("=")
            dic[my_list[0]]=my_list[1].strip("\n")
        return(dic)

ret = leer('file.txt')
print(ret)