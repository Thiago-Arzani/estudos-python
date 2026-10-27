# Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.

numero = int(input("Insira um número para ver sua tabuada de 1 a 10: "))

for i in range(1 ,11):
    print(i*numero)