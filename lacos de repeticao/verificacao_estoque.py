# Exercício 3: Verificação de Estoque Crítico (Setor de Logística): dada a lista de produtos
# estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
# A lista correspondente de quantidades:
# estoque_quantidades = [5, 12, 2, 8, 15].
# O estoque mínimo para qualquer item é 8 unidades. Crie um programa que percorra as listas e, para cada item que esteja abaixo do mínimo, imprima: "ALERTA: O produto [nome] está com apenas [quantidade] unidades no estoque!".

estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"]
estoque_quantidades = [5, 12, 2, 8, 15]


for i in range(len(estoque_quantidades)):
    if estoque_quantidades[i] < 8:
        print(f"ALERTA: O produto {estoque_produtos[i]} está com apenas {estoque_quantidades[i]} unidades no estoque!")