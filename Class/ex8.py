
def leer(arg):
    out = open('file.txt', 'w')
    for element in arg:
        out.writelines("valor="+element+"\n")
    out.close()


lista  = ['uno', 'dos','tres' ]

ret = leer(lista)

