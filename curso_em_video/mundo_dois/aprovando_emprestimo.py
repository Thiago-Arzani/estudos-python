# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("Bem-vindo! Verifique por aqui se você consegue a aprovação de um empréstimo bancário para sua casa.")
valor_casa = float(input("Primeiro, insira o valor da casa: R$ "))
salario = float(input("Agora, insira o seu salário: R$ "))
duracao_anos = float(input("Por fim, digite em quantos anos você vai pagá-lo: "))

duracao_meses = duracao_anos * 12
parcela = valor_casa / duracao_meses

if parcela > salario*0.30:
    print(f'Para pagar uma casa de R$ {valor_casa} em {duracao_anos} anos, a prestação será de R$ {parcela:.2f}, excedendo 30% do seu salário. Empréstimo NEGADO.')
else:
    print(f'Para pagar uma casa de R$ {valor_casa} em {duracao_anos} anos, a prestação será de R$ {parcela:.2f}. Empréstimo APROVADO!')