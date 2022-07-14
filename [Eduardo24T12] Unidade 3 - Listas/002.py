votes = [
   {
      "system": "Windows",
      "votes": 0
   },
   {
      "system": "Unix",
      "votes": 0
   },
   {
      "system": "Linux",
      "votes": 0
   },
   {
      "system": "Netware",
      "votes": 0
   },
   {
      "system": "MacOS",
      "votes": 0
   },
   {
      "system": "Outro",
      "votes": 0
   }
]

i = 0
totalVotos = 0
while i < 1:
   voto = int(input())

   if voto < 0 or voto > 6:
      print('Voto deve ser entre 1 e 6')
      break

   if voto == 0:
      i = 1
      break

   votes[voto - 1]["votes"] += 1;
   totalVotos += 1

porcentagens = []

for item in votes:
   porcentagem = (100 * item["votes"]) / totalVotos
   porcentagens.append(porcentagem)
   if item["votes"] != 0:
      if item["votes"] == 1:
         print(f'{item["system"]}, {item["votes"]} voto, {porcentagem:.0f}%')
      else:
         print(f'{item["system"]}, {item["votes"]} votos, {porcentagem:.0f}%')


if totalVotos == 1:
   print('Total: 1 voto')
else:
   print(f'Total: {totalVotos} votos')


for item in porcentagens:
   porcentagens[porcentagens.index(item)] = int(item)

maiorPorcentagem = max(porcentagens)

if porcentagens.count(maiorPorcentagem) == 1:
   i = porcentagens.index(maiorPorcentagem)

   print(f'Vencedor: {votes[i]["system"]} com {maiorPorcentagem}% dos votos')
else:
   for i in range(6):
      if porcentagens[i] == maiorPorcentagem:
         print(f'Vencedor: {votes[i]["system"]} com {maiorPorcentagem}% dos votos ')