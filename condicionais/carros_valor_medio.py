# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

# variáveis com input dos preços

ano_um = float(input("""
Insira o valor deste carro no primeiro ano: """))
ano_dois = float(input("""
Agora, o valor do mesmo carro no segundo ano: """))
ano_tres = float(input("""
Por fim, o preço dele no terceiro ano: """))

# condicionais para o maior valor

atual_maior = ano_um

if ano_dois > atual_maior:
    atual_maior = ano_dois

if ano_tres > atual_maior:
    atual_maior = ano_tres

print(atual_maior)