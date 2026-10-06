# Crie um programa que solicite dois valores numéricos, um numerador e um denominador e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numerador = float(input("Insira um numerador: "))
denominador = float(input("Agora insira um denominador diferente de zero: "))

if (denominador == 0):
    print("O denominador não pode ser zero.")
else:
    resto = float(numerador%denominador)
    print(f'O resultado é {numerador/denominador}, o resto é {resto}')
