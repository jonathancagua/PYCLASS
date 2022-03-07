def es_par(arg1):
    if arg1 % 2 == 0:
        return True 
    else:
        return False


r = es_par(8)
if r == True:
    print('El número es par.')
else:
    print('El número es impar.')