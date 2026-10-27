# Crie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

print("Calcule a média entre duas notas (de 0 a 10) de um estudante. \n")

primeira_nota = float(input("Insira a primeira nota deste aluno: "))
segunda_nota = float(input("Agora, a segunda nota dele: "))

media = (primeira_nota + segunda_nota)/2

if media < 5.0:
    print(f"Este aluno possui média {media}, e infelizmente está reprovado.")
elif media >= 5.0 and media <= 6.9:
    print(f"Este aluno possui média {media} e está em recuperação.")
elif media > 7.0 and media <= 10.0:
    print(f'O aluno está aprovado, com média {media}.')
elif media > 10.0:
    print("A nota é maior que 10. Refaça o cálculo.")