
def escribir(arg):
    out = open('file.txt', 'w')
    for k, v in arg.items():
        out.writelines(k +"="+v+"\n")
    out.close()

dic = {'ip': '192.168.0.1', 'nombre': 'Juan', 'estado': 'ON', 'color': '#555555', 'log': '3M'}
ret = escribir(dic)

