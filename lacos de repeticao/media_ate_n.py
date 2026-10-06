numero = int(input("Insira o numero: "))

i = 0
soma = 0

while i < numero:
    i = i + 1
    soma = i + soma

media = soma/i

print(soma)
print(media)