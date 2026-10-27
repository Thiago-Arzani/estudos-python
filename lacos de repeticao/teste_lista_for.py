numero_escolhido = int(input("Escolha um número: "))

lista = []
for i in range(numero_escolhido + 1):

    lista.append(i)

lista.pop()
print(lista)