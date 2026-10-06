# Inputs dos coeficientes

a = float(input("Insira o coeficiente a: "))
b = float(input("Insira o coeficiente b: "))
c = float(input("Insira o coeficiente c: "))

# Fórmulas dentro de variáveis

delta = b**2 - 4*a*c

x1 = ((-b) + (delta**0.5))/(2 * a)

x2 = ((-b) - (delta**0.5))/(2 * a)

# Condicionais para o resultado

if delta < 0:
    print("Como delta é menor que zero, x não possui raízes reais.")
elif delta == 0:
    print(f"A raíz é {x1:.3f}")
elif delta > 0:
    print(f"As raízes são {x1:.3f} e {x2:.3f}.")


