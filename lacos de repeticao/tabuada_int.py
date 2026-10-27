# Peça para o usuário digitar um número inteiro. Use um laço while para exibir a tabuada desse número de 1 a 10 no formato X * 1 = X.

numero = int(input("Insira um número para ver sua tabuada: "))

i = 1

while i <= 10: # enquanto i for menor que 10...
    resultado = i * numero # ...faça a conta: resultado = parte da tabuada vezes o número escolhido
    print(f" {i} * {numero} = {resultado}") # print dessa conta, no modelo descrito no enunciado
    i += 1 # aqui há a progressão na tabuada