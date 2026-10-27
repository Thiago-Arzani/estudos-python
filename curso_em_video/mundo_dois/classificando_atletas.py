# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima: Master

from datetime import date
ano_atual = date.today().year

nascimento = int(input("Insira abaixo a data de nascimento do atleta para descobrir sua categoria: \n"))
idade = ano_atual - nascimento

if idade <= 9:
    print(f'O atleta possui {idade} anos, classificando-se na categoria mirim.')
elif idade > 9 and idade <= 14:
    print(f'O atleta possui {idade} anos, classificando-se na categoria infantil.')
elif idade > 14 and idade <= 19:
    print(f'O atleta possui {idade} anos, classificando-se na categoria junior.')
elif idade > 19 and idade <= 25:
    print(f'O atleta possui {idade} anos, classificando-se na categoria sênior.')
elif idade > 25:
    print(f'O atleta possui {idade} anos, classificando-se na categoria master.')