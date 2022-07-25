nome = input()

def imprimirNomeEmEscadinha(texto):
    partes = ''
    for letra in texto:
        partes += letra
        print(partes)

imprimirNomeEmEscadinha(nome)