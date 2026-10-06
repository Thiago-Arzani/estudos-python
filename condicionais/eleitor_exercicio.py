"""Escreva um programa que calcula a idade de uma pessoa a partir do seu ano de nascimento. O programa também deve ler a nacionalidade da pessoa e mostrar na tela a idade e também as seguintes mensagens, quando for o caso:

Se a nacionalidade for brasileira, mostrar as mensagens:
"Já pode votar"  (se tiver 16 anos ou mais)

"Já pode solicitar a Carteira de Habilitação" (se tiver 18 anos ou mais)

Se for estrangeira:
"Verifique as regras do país onde você vota ou pretende tirar a carteira de habilitação"
Entrada

O programa deve ler do teclado um valor inteiro que corresponde ao ano de nascimento da pessoa e uma string indicando a nacionalidade da pessoa (considere que todas as letras lidas serão minúsculas).

Saída

O programa deve imprimir, primeiramente, a idade, no seguinte formato: "Você tem x anos", em que x é a idade da pessoa. Em seguida, na próxima linha, se a pessoa for brasileira e tiver idade para votar, imprimir "Já pode votar". Se tiver mais de 18 anos e for brasileira, além da mensagem anterior, deve imprimir também na linha seguinte "Já pode solicitar a Carteira de Habilitação".

Se a pessoa for estrangeira, após imprimir a idade, deverá imprimir a mensagem, na linha seguinte:  "Verifique as regras do país onde você vota ou pretende tirar a carteira de habilitação";"""

ano_nascimento = int(input('''
Insira o ano em que você nasceu: '''))
nacionalidade = input("""
Agora, insira sua nacionalidade em letras minúsculas:
""").lower()

idade = 2026 - ano_nascimento
print(f'Você tem {idade} anos.')

if nacionalidade == 'brasileira' and idade >= 18:
    print('Já pode votar')
    print('Já pode solicitar a Carteira de Habilitação')
elif nacionalidade == 'brasileira' and idade >= 16:
    print('Já pode votar')
elif nacionalidade != 'brasileira':
    print('Verifique as regras do país onde você vota ou pretende tirar carteira de habilitação.')
