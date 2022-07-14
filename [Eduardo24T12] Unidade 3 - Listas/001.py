nomes = []
notas = []

for i in range(5):
   nomes.append(input())
   notas.append(float(input()))

media = 0

for nota in notas:
   media += nota

media /= 5

print(f'Média: {media:.1f}')

acimaDaMedia = ''
for i in range(5):
   if notas[i] > 7:
      acimaDaMedia += f'{nomes[i]},'

acimaDaMedia = acimaDaMedia[:-1]


print(f'Acima da média: {acimaDaMedia}')

maiorNota = max(notas)
pessoaComMaiorNota = nomes[notas.index(maiorNota)]

print(f'Maior nota: {pessoaComMaiorNota}')