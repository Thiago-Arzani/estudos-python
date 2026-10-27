# Escreva um programa que receba várias notas de alunos. O programa deve parar de pedir notas apenas quando o usuário digitar -1. No final, calcule e exiba a média aritmética de todas as notas válidas digitadas.

nota = float(input("Digite as notas do aluno uma por vez. Caso tenha acabado, digite -1 \n"))

if nota < 0:
    print("Não tem como a nota ser menor que 0.")
elif nota > 10:
    print("Não tem como a nota ser maior que 10.")

else: 
    
    i = 0
    soma = 0

    while nota != -1:

        if nota < 0:
            print("Não tem como a nota ser menor que 0.")
            break
        elif nota > 10:
            print("Não tem como a nota ser maior que 10.")
            break

        else: nota = float(input("Agora, as próximas notas do aluno. Digite -1 caso tenha acabado. \n"))

        i += 1
        soma += nota

        if nota == -1:
            media = soma/i
            print(f"A média das notas é de {media}")



        
       
    








        
        

