# Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual = float(input("Insira o percentual de crescimento: "))

if(percentual == 0):
    print("Não houve crescimento ou decréscimo.")
elif(percentual > 0):
    print("Houve crescimento na produção.")
else:
    print("Houve um decréscimo na produção.")
