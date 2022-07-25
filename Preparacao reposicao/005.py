qtdTipos = int(input())

qtdBacteriasNoFim = []

for i in range(qtdTipos):
    qtdPorDivisao = int(input())
    dias = int(input())

    qtdBacteriasNoFim.append(qtdPorDivisao ** dias)

maiorQtdBacterias = max(qtdBacteriasNoFim)

print(qtdBacteriasNoFim.index(maiorQtdBacterias))