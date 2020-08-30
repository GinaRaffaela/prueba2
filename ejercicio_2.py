frase = input('ingrese una frase:')
letra = input('ingrese una letra:')
contador = 0
for i in range(len(frase)):
    if frase[i] == letra:
        contador = contador+1
print('Numero de veces que aparece la letra  {} en la frase {}: {}'.format(letra,frase,contador))

