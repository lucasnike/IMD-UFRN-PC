def truncate(num, n):
    integer = int(num * (10**n)) / (10**n)
    return float(integer)

capital = float(input())
taxa = float(input())
meses = int(input())

for i in range(meses):
   lucro = capital * (taxa/100)
   lucro = truncate(lucro, 2)
   print(f'mês: {i + 1}')
   print(f'saldo anterior: {truncate(capital, 2):.2f}')
   print(f'juros mês: {lucro:.2f}')
   capital += lucro
   print(f'novo saldo: {truncate(capital, 2):.2f}')

   if i != meses - 1:
      print('-')