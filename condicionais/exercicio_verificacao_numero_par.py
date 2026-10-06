# Faça um programa que recebe UM número e verifica se ele é par.

numero = int(input("""
Insira seu número e verifique se é par: """))

resto = numero % 2

if resto == 1:
    print("Este número é ímpar.")
else:
    print("Este número é par.")
