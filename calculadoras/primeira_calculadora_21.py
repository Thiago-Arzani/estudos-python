def soma(x, y):
    resultado = x + y
    return resultado

def subtracao(x, y):
    resultado = x - y
    return resultado

def multiplicacao(x, y):
    return (x * y)

def divisao(x, y):
    return (x / y)

print('=======Bem vindo à calculadora do Thiago!=======\n================================================')
primeiro_numero = float(input("Primeiro número: "))
print("""Operações: 

soma,
subtração, 
multiplicação, 
divisão
""")
operacao = input("Qual operação deseja? ")
segundo_numero = float(input("Segundo número: "))

if(operacao == "soma"):
    if(primeiro_numero == 9 and segundo_numero == 10):
        print(21)
    else:
        print(soma(primeiro_numero, segundo_numero))

if(operacao == "subtração"):
    print(subtracao(primeiro_numero, segundo_numero))

if(operacao == "multiplicação"):
    print(multiplicacao(primeiro_numero, segundo_numero))

if(operacao == "divisão"):
    print(divisao(primeiro_numero, segundo_numero))



