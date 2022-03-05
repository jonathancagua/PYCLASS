import csv
 
def ingresar_lista(arg):
    for element in arg:
        writer.writerow({'name':element[0], 'address':element[1], 'age':element[2]})

with open('example.csv', 'w') as File:  
    fieldnames = ['name','address','age']
    l = [('George', '4312 Abbey Road', 22), ('Juan', '54 Love Ave', 21),('Jaen', 'alborada', 19), ('Carlos', 'Sauces', 18)]

    writer = csv.DictWriter(File,fieldnames=fieldnames)
    writer.writeheader()
    ingresar_lista(l)