# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.

from datetime import date

nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

if nascimento > 2008:
    print(f'Você tem {idade} anos, ainda não precisando se alistar. Seu alistamento acontecerá em {18 - idade} anos, no ano de {nascimento + 18}.')
    
elif nascimento < 2008:
    print(f'Você tem {idade} anos e deveria ter se alistado há {2026 - (nascimento + 18)} anos, no ano de {nascimento + 18}.')

elif nascimento == 2008:
    print(f'Com {idade} anos, você deve se alistar imediatamente.')

