#Crie um programa que lê um valor inteiro positivo n e imprime a soma das potências de
#1 a n, isto é, (1^2 + 2^2 + 3^2) + · · · + n^2

n = int(input("Insira o valor N positivo: "))

while n < 0:
    print("Não pode ser negativo, tente novamente.")
    n = int(input("Insira o valor N positivo: "))
else:
    i = 0
    soma = 0 + 0

    while i < n:
        i = i + 1
        soma = i**2 + soma

print(soma)