n = int(input())
nSeq = []
for i in range(n):
   nSeq.append(int(input()))


m = int(input())
mSeq = []
for i in range(m):
   mSeq.append(int(input()))

def checkSequences(seq1, seq2):
   seq1Str = ''
   seq2Str = ''
   for item in seq1:
      seq1Str += str(item)


   for item in seq2:
      seq2Str += str(item)

   if seq1Str in seq2Str:
      print('S')
   else:
      print('N')

   for p in range(len(seq2) - 1):
      if ((p + 1) + len(seq1)) > len(seq2):
         print('Saiu')
         return False
      
      # if seq1[0] == seq2[p]:
      #    while 
      
      for i in range(len(seq1) - 1):
         x = seq1[i]
         y = seq2[p]

         if x != y:
            print('Diferente')
            # return False
         else:
            print('Igual')
            # return True

checkSequences(nSeq, mSeq)