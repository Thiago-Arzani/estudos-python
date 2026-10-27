# Cálculo de Comissão Progressiva (Setor de Vendas): você tem uma lista de vendas de um vendedor: vendas = [2000, 5000, 1000, 8000, 3000]. A regra de comissão é:
# Vendas acima de R$ 4.000,00: comissão de 10%.
# Vendas até R$ 4.000,00: comissão de 5%.
# Crie um programa que percorra a lista e, ao final, exiba o valor total que o vendedor receberá de comissão.

vendas = [2000, 5000, 1000, 8000, 3000]
comissao = 0

for valor in vendas:


    if valor <= 4000:
        resultado = valor*0.05
    
    
    elif valor > 4000:
        resultado = valor*0.1

    comissao += resultado




print(comissao)

