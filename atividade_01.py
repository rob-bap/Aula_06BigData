medias = []

for i in range(2):
    print(f"\nAluno {i + 1}")
    lista_notas = []

    for n in range(4):
        nota = float(input(f"\nDigite a nota número {n + 1}: "))
        lista_notas.append(nota)

    nota_total = sum(lista_notas)
    media = nota_total / 4
    MEDIA = 7

    medias.append(media)

for i, media in enumerate(medias):

    if media >= MEDIA:
        print(f"\nMédia do aluno {i + 1} é: {media}")
        print("Situação: aprovado")

    else:
        print(f"\nMédia do aluno {i + 1} é: {media}")
        print("Situação: reprovado")