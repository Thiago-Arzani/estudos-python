# Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

# variáveis com input dos preços

valor_um = float(input("""
Insira o valor deste carro no primeiro ano: """))
valor_dois = float(input("""
Agora, o valor do mesmo carro no segundo ano: """))
valor_tres = float(input("""
Por fim, o preço dele no terceiro ano: """))
valor_quatro = float(input("""
Eu menti, coloque mais um número: """))

# condicionais para o maior valor

atual_maior = valor_um

if valor_dois > atual_maior:
    atual_maior = valor_dois
if valor_tres > atual_maior:
    atual_maior = valor_tres
if valor_quatro > atual_maior:
    atual_maior = valor_quatro

print(f'O maior valor dentre os quatro anos foi de {atual_maior}.')

# condicionais para o menor valor

atual_menor = valor_um

if valor_dois < atual_menor:
    atual_menor = valor_dois
if valor_tres < atual_menor:
    atual_menor = valor_tres
if valor_quatro < atual_menor:
    atual_menor = valor_quatro

print(f'O menor valor foi de {atual_menor}')

if valor_um == 0 and valor_dois == 0 and valor_tres == 0:
    print("""
    Seu carro provavelmente é um Peugeot.
    """)