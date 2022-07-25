numeroDeRotulos = int(input())
qtdTipos = int(input())

quantidades = []

for i in range(qtdTipos):
    quantidades.append(0)


for i in range(numeroDeRotulos):
    tipo = int(input())
    quantidades[tipo - 1] += 1

qtdEnvelopes = min(quantidades)

print(qtdEnvelopes)