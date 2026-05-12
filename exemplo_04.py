lista_numeros = [7, 8, 5, 13, 2]
total = sum(lista_numeros)  # "sum" soma todos os elementos da uma lista
qta_total = len(lista_numeros)  # "len" conta quantos elementos há em uma lista
print(total, qta_total)


lista_produtos = ["notebook", "mouse", "teclado", "monitor"]

# exemplo 1
for n in range(4):
    print(lista_produtos[n])

# exemplo 2
for p in lista_produtos:
    print(p)

# exemplo 3
for i, p in enumerate(lista_produtos, start=1):
    print(i, p)
