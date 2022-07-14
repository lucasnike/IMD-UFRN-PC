m = int(input())
d = int(input())

fib = [1, 1]
fib2 = []

count = 0

i = 0
while i < 1:

   if d == 1:
      print('Sequência infinita')
   
   
   fib.append(fib[0] + fib[1])
   fib.pop(0)

   if fib[-1] % d == 0:
      fib2.append(fib[-1])
      count += 1
   
   # Termina o loop
   if count == m:
      i = 1
      break
   

for item in fib2:
   print(item)