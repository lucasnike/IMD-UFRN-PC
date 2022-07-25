tamanho_da_lista = int(input())

valores = []

for i in range(tamanho_da_lista):
    valores.append(int(input()))

valores = set(valores)
valores = list(valores)

valoresSemRepeticao = ''
for valor in valores:
    valoresSemRepeticao += str(valor)

    if valores[-1] != valor:
        valoresSemRepeticao += ' '

print(valoresSemRepeticao)