numero = int(input())

divisores = []

for i in range(numero):
   if numero % (i + 1) == 0:
      divisores.append(i + 1)

divisores.pop()

soma = 0

for item in divisores:
   soma += item;

if soma == numero:
   print('número perfeito')
else:
   print('número não é perfeito')