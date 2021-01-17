print('========= CALCULADORA =========')

while True:
    r = ''
    a = 0
    numero = 0
    numeros = []
    atual = '0'
    resultado = 0

    print('\nPressione \033[31m0\033[m para: \033[34msomar\033[m')
    print('Pressione \033[31m1\033[m para: \033[34msubtrair\033[m')
    print('Pressione \033[31m2\033[m para: \033[34mdividir\033[m')
    print('Pressione \033[31m3\033[m para: \033[34mmultiplicar\033[m')
    print('Pressione \033[31m4\033[m para: \033[34mraiz quadrada\033[m')
    print('Pressione \033[31m5\033[m para: \033[34márea geométrica\033[m')
    print('Pressione \033[31m6\033[m para: \033[34msair\033[m')

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
        print('\n\033[31m1 : para Calcular a área do Quadrado')
        print('2 : para Calcular a área do Retângulo')
        print('3 : para Calcular a área do Paralelogramo')
        print('4 : para Calcular a área do Trapézio')
        print('5 : para Calcular a área do losangulo')
        print('6 : para Calcular a área do Triângulo\033[m')

        try:
            a = int(input(': '))
        except:
            print(end='')

        if (a == 1):

            print('\nPara se calcular a área do Quadrado')
            print('pegue a medida de um lado e multiplique')
            print('por ele mesmo\n')

            try:
                h = float(input('Altura do quadrado: '))
            except:
                print(end='')

            print(f'\nA área do quadrado é igual a \033[31m{h * h}\033[m')

        elif (a == 2):

            print('\nPara se calcular a área do Retângulo')
            print('pegue a medida da altura e da base')
            print('e multiplique altura * base\n')

            try:
                b = float(input('Base do Retângulo: '))
            except:
                print(end='')
            try:
                h = float(input('Altura do Retângulo: '))
            except:
                print(end='')

            print(f'\nA área do Retângulo é igual a \033[31m{b * h}\033[m')

        elif (a == 3):

            print('\nPara se calcular a área do Paralelogramo')
            print('é semelhante ao Retângulo, altura * largura\n')

            try:
                b = float(input('Base do Paralelogramo: '))
            except:
                print(end='')
            try:
                h = float(input('Altura do Paralelogramo: '))
            except:
                print(end='')

            print(f'\nA área do Paralologramo é igual a \033[31m{b * h}\033[m')
        elif (a == 4):

            print('\nPara se calcular a área do Trapézio')
            print('some base menor e base maior multiplique')
            print('pela altura e divida por 2\n')

            try:
                b = float(input('Base menor do Trapézio: '))
            except:
                print(end='')
            try:
                b += float(input('Base maior do Trapézio: '))
            except:
                print(end='')
            try:
                h = float(input('Altura do do Trapézio: '))
            except:
                print(end='')

            print(f'\nA área do Trapézio é igual a \033[31m{(b * h) / 2}\033[m')
        elif (a == 5):
            print('\nPara se calcular a área do Losangulo')
            print('Transforme-o em um Paralelogramo e')
            print('pegue a altura e base multiplique')
            print('altura * base e depois divida por 2\n')

            try:
                b = float(input('Base do Losangulo: '))
            except:
                print(end='')
            try:
                h = float(input('Altura do Losangulo: '))
            except:
                print(end='')

            print(f'\nA área do Losangulo é igual a \033[31m{(b * h) / 2}\033[m')
        elif (a == 6):
            print('\nPara se calcular a área do Triângulo')
            print('transforme-o em um Paralelogramo pegue')
            print('a altura e a base e multiplique')
            print('depois divida-o por 2\n')

            try:
                b = float(input('Base do Triângulo: '))
            except:
                print(end='')
            try:
                h = float(input('Altura do Triângulo: '))
            except:
                print(end='')

            print(f'\nA área do Triângulo é igual a \033[31m{(b * h) / 2}\033[m')

    if r == '6':
        break

print('FIM!!')
