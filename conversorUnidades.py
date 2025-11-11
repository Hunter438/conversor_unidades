from time import sleep
def converterTemp():
    celsius = float(input('Digite a temperatura para a conversão em fahrenheit: '))
    fahr = celsius * 1.8 + 32
    print(f'O resultado da conversão de {celsius:.2f}º para fahrenheit é {fahr:.2f}º.')
def converterMetro():
    metro = float(input('Digite o tamanho (em metros) para a conversão em Cm: '))
    cent = metro * 100
    print(f'O tamanho de {metro} metros convertido para Cm é {cent} centímetros.')
def converterHora():
    hora = float(input('Digite as horas para converter em minutos: '))
    min = hora * 60
    print(f'{hora} convertido para minutos é {min}.')

def menu():
    print('-' * 40)
    print('CONVERSOR DE UNIDADES'.center(40))
    print('1- Converter Celsius para Fahrenheit')
    print('2- Converter Metros para Centímetros')
    print('3- Converter Horas para Minutos')
    print('0- Sair')
    print('-' * 40)

while True:
    menu()
    try:
        opc = int(input('Escolha uma opção: '))
    except ValueError:
        print('Entrada inválida! Digite um número (0 a 3): ')
        continue

    if opc == 1:
        converterTemp()
        sleep(2)
    elif opc == 2:
        converterMetro()
        sleep(2)
    elif opc == 3:
        converterHora()
        sleep(2)
    elif opc == 0:
        print('Volte sempre!')
        sleep(2)
        break
    else:
        print('Opção inválida!')
        break