# O programa deve escolher um número secreto (você pode fixar um número como 7). O usuário deve tentar adivinhar o número. Enquanto ele errar, o programa deve dizer se o palpite foi "Maior" ou "Menor" que o número secreto e pedir um novo palpite. O jogo acaba quando ele acertar.

print("\n Adivinhe o número que escolhi para vencer.")

print("Escolha um número agora, e te direi se ele é maior ou menor do que o número que escolhi.\n")
tentativa = float(input())

while tentativa != 7:
    if tentativa > 7:
        print("ERRADO! Meu número é MENOR que este. Tente de novo.")
        tentativa = float(input())
    elif tentativa < 7:
        print("ERRADO! Meu número é MAIOR que este. Tente de novo.")
        tentativa = float(input())

    

    
if tentativa == 7:
    print("Parabéns, era 7!")    
