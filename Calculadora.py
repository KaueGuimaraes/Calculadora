print('========= CALCULADORA =========\n')

r = ''
numero = 0
numeros = []
resultado = 0

print('Pressione 0 para: somar')
print('Pressione 1 para: subtrair')
print('Pressione 2 para: dividir')
print('Pressione 3 para: multiplicar')
print('Pressione 4 para: taiz quadrada')

r = str(input(': '))

if r == '0':
    numero = int(input('Quantos números?'))
    numeros = []

    for c in range(0, numero):
        numeros.append(int(input(f"{c + 1} número: ")))

    for c in range(0, len(numeros)):
         if(c == len(numeros) - 1):
             print(f'{numeros[c]}', end='')
         else:
             print(f'{numeros[c]} + ', end='')
         numero += numeros[c]

    print(f' = {numero}')