metrosCubicos = int(input())

def calcularContaDeAgua(metros):
    total = 7
    if metros > 10 and metros <= 30:
        total += metros - 10

    if metros > 30 and metros < 101:
        total += 20
        total += (metros - 30) * 2

    if metros > 100:
        total += 160
        total += (metros - 100) * 5

    return total

print(calcularContaDeAgua(metrosCubicos))