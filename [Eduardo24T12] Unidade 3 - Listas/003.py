l1 = []
l2 = []

for i in range(5):
   l1.append(int(input()))

for i in range(5):
      l2.append(int(input()))

l1.extend(l2)
l1.sort()

finalText = ''

for i in range(10):
   if i == 9:
      finalText += str(l1[i])
      break

   finalText += str(l1[i]) + ' '

print(finalText)