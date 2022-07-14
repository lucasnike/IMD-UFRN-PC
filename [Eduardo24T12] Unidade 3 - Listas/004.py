numeroDeMontanhas = int(input())

altitudeMontanhas = []

for i in range(numeroDeMontanhas):
   altitudeMontanhas.append(int(input()))

indiceMontanhaAtual = int(input())
montanhaAtual = altitudeMontanhas[indiceMontanhaAtual]

distancias = [1]

for i in range(numeroDeMontanhas):
   distancia = (10 * montanhaAtual) + (10 * altitudeMontanhas[i]) + abs((indiceMontanhaAtual - i) * 10)
   distancias.append(distancia)


distancias.remove(1)
print(distancias.index(min(distancias)))