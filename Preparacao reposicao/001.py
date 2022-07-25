def formatarNumero(numero, digitos):
    numero = int(numero * (10 ** digitos))
    numero = numero / (10 ** digitos)
    return numero

n = int(input())
notas = []

media = 0

for i in range(n):
    nota = float(input())
    notas.append(nota)
    media += nota

media = formatarNumero(media / n, 2)

notasAcimaMedia = 0

for nota in notas:
    if nota >= media:
        notasAcimaMedia += 1

print(f'Foram lidos {n} valores')
print(notas)
notas.reverse()
print(f'Lista reversa:  {notas}')
print(f'Média dos valores:  {media}')
print(f'{notasAcimaMedia} valores acima da média {media}')