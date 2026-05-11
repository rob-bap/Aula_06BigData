# contador = 0

# while contador < 4:
#     print(contador)
#     contador += 1

while True:
    numero = int(input("\nDigite um número: "))

    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2

    print(f"O dobro é {dobro}")
    print(f"O triplo é {triplo}")
    print(f"O quadrado é {quadrado}")

    # condição de parada para parar o 'while'

    resposta = input("\nGostaria de continuar? [Y/N]: ").upper().strip()[0]  # [0] pega só a primeira letra do input

    if resposta == "N":
        break