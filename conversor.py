print('='*50, 'Conversor de Bases Numéricas', '=' *50)
numero = int(input('Digite um número [DECIMAL]: '))
opcao_base = int(input(f'Digite a base que desja converter\n 1 [Binário]\n 2 [Octal]\n 3 [Hexadecimal]\n Base: '))


if opcao_base == 1:
    print('*' *50, 'Base Binária selecionada.', '*' *50)
    resultado = ''
    while numero > 0:
        resultado = str(numero % 2) + resultado  
        numero = numero // 2 
    print(f'O número {numero} [DECIMAL] em binário é:', resultado)
    print('=' *50, 'Fim', '=' *50)
elif opcao_base == 2:
    print('*' *50, 'Base Octal selecionada.', '*' *50)
    resultado = ''
    while numero > 0:
        resultado = str(numero % 8) + resultado  
        numero = numero // 8 
    print(f'O número {numero} [DECIMAL] em octal é:', resultado)
    print('=' *50, 'Fim', '=' *50)
elif opcao_base == 3:
    print('*' *50, 'Base Hexadecimal selecionada.', '*' *50)
    resultado = ''
    hex_digitos = {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
       15: 'F'
    }
    while numero > 0:
        resto = numero % 16
        if resto >= 10:
            resultado = hex_digitos[resto] + resultado
        else:
            resultado = str(resto) + resultado
        numero = numero // 16 
    print(f'O número [DECIMAL] em Hexadecimal é:', resultado)
    print('=' * 50, 'Fim', '=' * 50)
