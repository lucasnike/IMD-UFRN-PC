sistema = ['Windows', 'Unix','Linux','Netware','Mac OS','Outro']
contador = contadorPerc = 0
vencedor = ''
por = []
votos = [0,0,0,0,0,0]
vote = 10
while vote != 0:
    vote = int(input())
    if vote == 1:
        votos[0]+=1
        contador += 1
    elif vote == 2:
        votos[1]+=1
        contador += 1
    elif vote == 3:
        votos[2]+=1
        contador += 1
    elif vote == 4:
        votos[3]+= 1
        contador += 1
    elif vote == 5:
        votos[4]+=1
        contador += 1
    elif vote == 6:
        votos[5]+=1
        contador += 1
    elif 0:
        break
for i in range(len(votos)):
    por.append(int((votos[i]/contador)*100))
    if votos[i] > 0:
        print("{}, {} voto, {}%".format(sistema[i], votos[i], por[i]))
    elif votos[i] > 1:
        print("{}, {} votos, {}%".format(sistema[i], votos[i], por[i]))
print("Total: {} votos".format(sum(votos)))

# Alteração
maiorPorcentagem = max(por)
for i in range(len(por)):
    if por[i] == maiorPorcentagem:
        vencedor = (sistema[i])
        print(f"Vencedor: {vencedor} com {por[i]}%  dos votos ")