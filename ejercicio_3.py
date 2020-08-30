signo = '*'

try:
    numero = int(input('Ingrese un número: '))

    if numero <= 0:
        print('Debe ser un número mayor a 0 ')
    else:
        print()
        for i in range(numero + 1):
            print(signo * i)
except:
    print('Intente de nuevo')
    
print()
