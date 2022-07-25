def calcularQtdDeNotas(valor):
    notas100 = valor // 100
    valor -= notas100 * 100

    notas50 = valor // 50
    valor -= notas50 * 50

    notas20 = valor // 20
    valor -= notas20 * 20

    notas10 = valor // 10
    valor -= notas10 * 10

    notas5 = valor // 5
    valor -= notas5 * 5

    notas2 = valor // 2
    valor -= notas2 * 2

    notas1 = valor

    return {
        "notas100": notas100,
        "notas50": notas50,
        "notas20": notas20,
        "notas10": notas10,
        "notas5": notas5,
        "notas2": notas2,
        "notas1": notas1
    }

valor = int(input())

qtdNotas = calcularQtdDeNotas(valor)

print(f'{qtdNotas["notas100"]} de 100')
print(f'{qtdNotas["notas50"]} de 50')
print(f'{qtdNotas["notas20"]} de 20')
print(f'{qtdNotas["notas10"]} de 10')
print(f'{qtdNotas["notas5"]} de 5')
print(f'{qtdNotas["notas2"]} de 2')
print(f'{qtdNotas["notas1"]} de 1')
