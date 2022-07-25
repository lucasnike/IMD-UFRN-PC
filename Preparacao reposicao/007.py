participantes = int(input())
papeis = int(input())
papeisPorParticipante = int(input())

if (participantes * papeisPorParticipante) <= papeis:
    print('S')
else:
    print('N')