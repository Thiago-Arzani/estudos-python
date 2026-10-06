largura = float(input("Insira a largura do imóvel em metros: "))
comprimento = float(input("Insira o comprimento: "))
area = largura*comprimento
valor = float(input("Qual o valor do seu imóvel? "))
valor_metro_quadrado = valor/area
print(f'O valor do metro quadrado é {valor_metro_quadrado:.3f}')
