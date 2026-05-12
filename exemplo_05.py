total_vendas = []
media_vendas = []

for i in range(3):
    print(f"\nVendedor {i + 1}")

    quantidade = int(input("Digite a quantidade de vendas: "))
    vendas = []

    for n in range(quantidade):
        valor = float(input(f"\nInforme o valor da venda {n + 1}: "))
        vendas.append(valor)

    total = sum(vendas)
    media = total / quantidade  # ou total / len(vendas)
        
    total_vendas.append(total)
    media_vendas.append(media)

META = 1000
META_MINIMA = 700

print("\nRESULTADOS")
for i, media in enumerate(media_vendas):
    print(f"\nVededor {i + 1}")
    print(f"Total vendido: R${total_vendas[i]}")
    print(f"Média das vendas R${media:.2f}")

    if media >= META:
        print(f"Meta de R${META} foi atingida.")

    elif media >= META_MINIMA:
        print(f"Meta mínima de R${META_MINIMA} foi atingia. ")
    
    else:
        print("Meta não foi atingida.")