lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1:
   print('possível')
else:
   print('impossível')