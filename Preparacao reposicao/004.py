maximo = int(input())

valor1 = int(input())
operador = input()
valor2 = int(input())

resultado = 0

if operador == '+':
    resultado = valor1 + valor2
else:
    resultado = valor1 * valor2

if resultado <= maximo:
    print('OK')
else:
    print('OVERFLOW')