tempoMinimo = float(input())

temposDosAtletas = []

i = 0
while i < 1:
   tempoAtleta = float(input())

   if tempoAtleta == -1:
      i = 1

   if tempoAtleta <= tempoMinimo and tempoAtleta >= 0:
      temposDosAtletas.append(tempoAtleta)
   

qtdAtletasAptos = len(temposDosAtletas)

print(qtdAtletasAptos)
qtdSeries = 0

if qtdAtletasAptos < 8 and qtdAtletasAptos >= 1:
   print(1)
   exit()
elif qtdAtletasAptos >= 8:
   qtdSeries = qtdAtletasAptos // 8

if qtdAtletasAptos == 0:
   print(0)
   exit()

if qtdAtletasAptos % 8 != 0:
   qtdSeries += 1

print(qtdSeries)