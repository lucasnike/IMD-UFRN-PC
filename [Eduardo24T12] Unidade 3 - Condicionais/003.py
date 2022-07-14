import datetime
ano = int(input())

anoAtual = datetime.date.today().year

idade = anoAtual - ano

if idade < 16:
   print(f'{idade} anos')
   print('Não pode votar e não pode dirigir')
elif idade >= 16 and idade < 18:
   print(f'{idade} anos')
   print('Pode votar e não pode dirigir')
elif idade > 17:
   print(f'{idade} anos')
   print('Pode votar e dirigir')