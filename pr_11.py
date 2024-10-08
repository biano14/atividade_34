import os
#funções
def mostrar_menu():
    print('1 - Calcular quadrilétero.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Calcular Trapezio.')
    print('5 - Sair do programa.')
    
def calcular_quadrilatero(b ,h):
    result = b * h
    return result

def calcular_triangulo(b, h):
    result = (b * h)/2
    return result

def calcular_circulo(r):
    result = 3.14*r**2
    return result

def calcular_trapesio(b,bg,h):
    result = ((b + bg) * h)/h
    return result
    
#programa principal

while True:
    mostrar_menu()
    opcao = input('Opção desejada: ')
    match opcao:
        case '1':
            b = float(input('Informe o valor da base: ').replace(',','.'))
            h = float(input('Informe o valor da altura: ').replace(',','.'))
            os.system('cls')
            print(f'Área do quadrilátero: {calcular_quadrilatero(b, h)}')
            print('\n')
            continue
        case '2':
            b = float(input('Informe o valor da base: ').replace(',','.'))
            h = float(input('Informe o valor da altura: ').replace(',','.'))
            os.system('cls')
            print(f'Área do triângulo: {calcular_triangulo(b, h)}')
            print('\n')
            continue
        case '3':
            r = float(input('Informe o valor do raio: ').replace(',','.'))
            os.system('cls')
            print(f'Área da circunferência: {calcular_circulo(r)}.')
            print('\n')
            continue
        case '4':
            b = float(input('Informe o valor da base menor: ').replace(',','.'))
            bg = float(input('Informe o valor da base maior: ').replace(',','.'))
            h = float(input('Informe o valor da altura: ').replace(',','.'))
            os.system('cls')
            print(f'Área do Trapézio: {calcular_trapesio(b,bg, h)}.')
            print('\n')
            continue
        case '5':
            print('Programa encerrado.')
            break
        case _:
            print('Opção inválida.')