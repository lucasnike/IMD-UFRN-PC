camisas = [
   {
      "tipo": "A",
      "P": 10,
      "M": 7,
      "G": 5
   },
   {
      "tipo": "V",
      "P": 12,
      "M": 5,
      "G": 4
   },
]

tipo = input()
qtdP = int(input())
qtdM = int(input())
qtdG = int(input())

for camisa in camisas:
   if camisa["tipo"] == 'A':
      if camisa["tipo"] == tipo:
         if qtdP <= camisa["P"]:
            print(f'P(A):{camisa["P"] - qtdP}')
            camisa["P"] -= qtdP
         else:
            print(f'P(A):{camisa["P"]} - "Quantidade não disponível".')
         
         if qtdM <= camisa["M"]:
            print(f'M(A):{camisa["M"] - qtdM}')
            camisa["M"] -= qtdM
         else:
            print(f'M(A):{camisa["M"]} - "Quantidade não disponível".')

         if qtdG <= camisa["G"]:
            print(f'G(A):{camisa["G"] - qtdG}')
            camisa["G"] -= qtdG
         else:
            print(f'G(A):{camisa["G"]} - "Quantidade não disponível".')

         
      else:
         print(f'P(A):{camisa["P"]}')
         print(f'M(A):{camisa["M"]}')
         print(f'G(A):{camisa["G"]}')
   elif camisa["tipo"] == 'V':
      if camisa["tipo"] == tipo:
         if qtdP <= camisa["P"]:
            print(f'P(V):{camisa["P"] - qtdP}')
            camisa["P"] -= qtdP
         else:
            print(f'P(V):{camisa["P"]} - "Quantidade não disponível.')
         
         if qtdM <= camisa["M"]:
            print(f'M(V):{camisa["M"] - qtdM}')
            camisa["M"] -= qtdM
         else:
            print(f'M(V):{camisa["M"]} - "Quantidade não disponível".')

         if qtdG <= camisa["G"]:
            print(f'G(V):{camisa["G"] - qtdG}')
            camisa["G"] -= qtdG
         else:
            print(f'G(V):{camisa["G"]} - "Quantidade não disponível".')
      else:
         print(f'P(V):{camisa["P"]}')
         print(f'M(V):{camisa["M"]}')
         print(f'G(V):{camisa["G"]}')