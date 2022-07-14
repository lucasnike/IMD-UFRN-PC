horas = int(input())
minutos = int(input())
segundos = int(input())


def formatarHora(h, m, s):
   horario = ''
   if h <= 9:
      horario = f'0{h}:'
   else:
      horario = f'{h}:'
   
   if m <= 9:
      horario += f'0{m}:'
   else:
      horario += f'{m}:'
   
   if s <= 9:
      horario += f'0{s}'
   else:
      horario += f'{s}'
   return horario

horario = formatarHora(horas, minutos, segundos)

def somarHoras(h1, h2):
   h1 = h1.split(':')
   h2 = h2.split(':')

   for i in range(3):
      h1[i] = int(h1[i])
      h2[i] = int(h2[i])

   for i in range(3):
      h1[i] = int(h1[i] + h2[i])

   if h1[2] >= 60:
      h1[1] += 1
      h1[2] -= 60
   
   if h1[1] >= 60:
      h1[0] += 1
      h1[1] -= 60
   
   if h1[0] >= 24:
      h1[0] -= 24

   horario = ''
   if h1[0] <= 9:
      horario = f'0{h1[0]}:'
   else:
      horario = f'{h1[0]}:'
   
   if h1[1] <= 9:
      horario += f'0{h1[1]}:'
   else:
      horario += f'{h1[1]}:'
   
   if h1[2] <= 9:
      horario += f'0{h1[2]}'
   else:
      horario += f'{h1[2]}'

   return horario


print(horario)
print(somarHoras(horario, '01:00:00'))
print(somarHoras(horario, '02:10:30'))
print(somarHoras(horario, '04:40:50'))
print(somarHoras(horario, '12:05:05'))