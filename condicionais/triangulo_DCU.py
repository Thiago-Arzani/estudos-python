""" Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;"""

lado_um = float(input("\nInsira o primeiro lado do triângulo: "))
lado_dois = float(input("\nInsira o segundo lado do triângulo: "))
lado_tres = float(input("\nInsira o terceiro lado do triângulo: "))

# lado um e dois
# lado um e tres
# lado dois e tres

if lado_um + lado_dois > lado_tres and lado_um + lado_tres > lado_dois and lado_dois + lado_tres > lado_um:
    print("Parabéns, você tem um triângulo")
    if lado_um == lado_dois == lado_tres:
        print("Seu triângulo é equilátero")
    if lado_um == lado_dois or lado_um == lado_tres or lado_dois == lado_tres:
        print("Seu triângulo é isósceles")
    if lado_um != lado_dois != lado_tres:
        "Seu triângulo é escaleno"

else:
    print("Você não tem um triângulo")