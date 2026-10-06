# Funções de cálculo

def somar(x, y):
    return (x + y)

def subtrair(x, y):
    return (x - y)

def multiplicar(x, y):
    return (x * y)

def dividir(x, y):
    return (x / y)

# Corpo do código

print("""
Bem vindo à calculadora (SOLO) do Thiago!
Com esta ferramenta, você consegue realizar cálculos simples com dois números.
""")

primeiro_numero = float(input("""Para começar, digite seu primeiro número: 
"""))

print("""
Que número bonito! Agora, selecione o número correspondente à operação que você deseja fazer:

1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir

""")

operacao = input("""Qual operação você quer fazer? 
""")

segundo_numero = float(input("""
Digite o segundo número: 
"""))

somar(primeiro_numero, segundo_numero)
subtrair(primeiro_numero, segundo_numero)
multiplicar(primeiro_numero, segundo_numero)
dividir(primeiro_numero, segundo_numero)

if(operacao == "1"):
    print(f'''
        Seu resultado é {somar(primeiro_numero, segundo_numero)}! Top demais!
        ''' )
if(operacao == "2"):
    print(f'''
        Seu resultado é {subtrair(primeiro_numero, segundo_numero)}! Top demais!
        ''' )
if(operacao == "3"):
    print(f'''
        Seu resultado é {multiplicar(primeiro_numero, segundo_numero)}! Top demais!
        ''' )
if(operacao == "4"):
    print(f'''
    Seu resultado é {dividir(primeiro_numero, segundo_numero)}! Top demais!
    ''' )

