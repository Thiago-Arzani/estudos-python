# Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

def dividir(x, y):
    return float((x / y))

numerador = float(input("""Insira um numerador: 
"""))
denominador = float(input("""Agora insira um denominador diferente de zero: 
"""))

if (denominador == 0):
    print("O denominador não pode ser zero.")
else: 
    print(f'O seu resultado é {dividir(numerador, denominador)}')
