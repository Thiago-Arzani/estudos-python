# Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

def media(x, y, z):
    return (x + y + z)/3

print("""
Calculadora de média entre três notas de disciplinas
""")
primeira_nota = float(input("""Qual é a primeira nota do aluno?
"""))
segunda_nota = float(input("""Agora, insira a segunda nota dele:
"""))
terceira_nota = float(input("""Por fim, a terceira nota:
"""))

resultado = media(primeira_nota, segunda_nota, terceira_nota)

print(f'A média entre essas notas deste aluno é de {resultado}')