# Programa para automatizar la venta de entradas

hombre = 10500
mujer = 8000
socio = 6000
cant_hombre = 0
cant_mujer = 0
cant_socio = 0
opcion = 0
fiesta = []
total = 0

while True:
    print(''' BIENVENIDO A LA FIESTA
          (1) Agregar Participantes a la Fiesta
          (2) Ver Integrantes de la Fiesta
          (3) Salir''')
    try:
        opcion = int(input('Digite una opción: '))
    except:
        print('Debe ingresar una opción válida')
        continue

    if opcion < 1 or opcion > 4:
        print('Debe ingresar una opción válida')
    elif opcion == 1:
        while opcion != 6:
            print('''Seleccione Participantes para la Fiesta
                  (1) Hombres ($ 10.500)
                  (2) Mujeres ($ 8.000)
                  (3) Socios ($ 6.000)''')
            try:
                opcion = int(input('Digite una opción: '))
            except:
                print('Debe ingresar una opción válida')
                continue
            if opcion < 1 or opcion > 6:
                print('Debe ingresar una opción válida')

            elif opcion == 1:
                try:
                    cantidad = int(input('Ingrese cantidad de Hombres: '))
                    if cantidad < 1:
                        print('Debe ingresar una cantidad válida')
                    else:
                        total = total + hombre*cantidad
                        cant_hombre += cantidad
                        print('Ha ingresado' ,cantidad, 'Hombres')
                        if 'hombre' not in fiesta:
                            fiesta.append('hombre')
                            break
                except:
                    print('Debe ingresar una cantidad válida')
                    continue

            elif opcion == 2:
                try:
                    cantidad = int(input('Ingrese cantidad de Mujeres: '))
                    if cantidad < 1:
                        print('Debe ingresar una cantidad válida')
                    else:
                        total = total + mujer*cantidad
                        cant_mujer += cantidad
                        print('Ha ingresado',cantidad, 'Mujeres')
                        if 'mujer' not in fiesta:
                            fiesta.append('mujer')
                            break
                except:
                    print('Debe ingresar una cantidad válida')
                    continue

            elif opcion == 3:
                try:
                    cantidad = int(input('Ingrese cantidad de Socios: '))
                    if cantidad < 1:
                        print('Debe ingresar una cantidad válida')
                    else:
                        total = total + socio*cantidad
                        cant_socio += cantidad
                        print('Ha ingresado',cantidad, 'Socios')
                        if 'socio' not in fiesta:
                            fiesta.append('socio')
                            break
                except:
                    print('Debe ingresar una cantidad válida')
                    continue                        
          
    elif opcion == 2:
        if len(fiesta) == 0:
            print('No hay Participantes en la Fiesta ')
        else:
            print('FIESTA')
            if 'hombre' in fiesta:
                print('Hombre (s):',cant_hombre, 'Total', cant_hombre*hombre)
            if 'mujer' in fiesta:
                print('Mujer (s):' , cant_mujer, 'Total', cant_mujer*mujer)
            if 'socio' in fiesta:
                print('Socio (s):', cant_socio, 'Total', cant_socio*socio)
            print('Total a pagar: $' ,total, 'pesos')

print()
