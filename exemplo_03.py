lista_produtos = ["notebook", "mouse", "teclado", "monitor"]

lista_produtos[0] = "PC"  # é possivel alterar membro da ista
lista_produtos.append("microfone")  # adiciona membro no final da lista
lista_produtos.insert(2, "fone")  # adicona membro na lista em uma determinada posição
lista_produtos.pop()  # apaga o ultimo membro da lista
lista_produtos.remove("monitor")  # remove membro da lista (não funciona apontando posição, pois verifica se o membro existe na lista)
lista_produtos.clear  # limpa tdos os membros da lista

del lista_produtos[0]  # metodo "perigoso" de apagar um membro da lista por sua posição

print(lista_produtos)