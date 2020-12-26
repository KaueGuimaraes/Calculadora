print('========= CALCULADORA =========')

while True:
    r = ''
    numero = 0
    numeros = []
    atual = '0'
    resultado = 0

    print('\nPressione \033[31m0\033[m para: \033[34msomar\033[m')
    print('Pressione \033[31m1\033[m para: \033[34msubtrair\033[m')
    print('Pressione \033[31m2\033[m para: \033[34mdividir\033[m')
    print('Pressione \033[31m3\033[m para: \033[34mmultiplicar\033[m')
    print('Pressione \033[31m4\033[m para: \033[34mraiz quadrada\033[m')
    print('Pressione \033[31m5\033[m para: \033[34msair\033[m')

    r = str(input(': '))

    if r == '0':
        print()
        while True:
            try:
                numero = int(input('Quantos números?'))
                break
            except:
                print(end='')
        numeros = []

        for c in range(0, numero):
            while True:
                atual = str(input(f'{c + 1} número: '))

                try:
                    numeros.append(float(atual))
                    break
                except:
                    print(end='')
        print()
        for c in range(0, len(numeros)):
            resultado += numeros[c]
            if c == len(numeros) - 1:
                print(f'{numeros[c]} = ', end='')
            else:
                print(f'{numeros[c]} + ', end='')

        print(resultado)

    if r == '1':
        print()
        while True:
            try:
                numero = int(input('Quantos números?'))
                break
            except:
                print(end='')
        numeros = []

        for c in range(0, numero):
            while True:
                atual = str(input(f'{c + 1} número: '))

                try:
                    numeros.append(float(atual))
                    break
                except:
                    print(end='')
        print()
        for c in range(0, len(numeros)):
                if c == 0:
                    resultado = numeros[c]
                else:
                    resultado -= numeros[c]

                if c == len(numeros) - 1:
                    print(f'{numeros[c]} = ', end='')
                else:
                    print(f'{numeros[c]} - ', end='')

        print(resultado)

    if r == '2':
        print()
        numeros = []

        for c in range(0, 2):
            while True:
                atual = str(input(f'{c + 1} número: '))

                try:
                    numeros.append(float(atual))
                    break
                except:
                    print()

        resultado = numeros[0] / numeros[1]
        print(f'{numeros[0]} / {numeros[1]} = {resultado}')

    if r == '3':
        print()
        while True:
            try:
                numero = int(input('Quantos números?'))
                break
            except:
                print(end='')
        numeros = []

        for c in range(0, numero):
            while True:
                atual = str(input(f'{c + 1} número: '))

                try:
                    numeros.append(float(atual))
                    break
                except:
                    print(end='')
        print()
        for c in range(0, len(numeros)):
            if c == 0:
                resultado = numeros[c]
            else:
                resultado *= numeros[c]

            if c == len(numeros) - 1:
                print(f'{numeros[c]} = ', end='')
            else:
                print(f'{numeros[c]} * ', end='')

        print(resultado)

    if r == '4':
        while True:
            atual = str(input('Número: '))

            try:
                numeros.append(float(atual))
                break
            except:
                print(end='')

        print(f'A raiz quadrada de {numeros[0]} é {numeros[0] ** (1/2)}')

    if r == '5':
        break
