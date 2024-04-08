import math

def calcular_raizes(a, b, c):
    # Calcula o discriminante
    delta = b**2 - 4*a*c

    # Verifica se a equação tem raízes reais
    if delta < 0:
        return None  # Equação não possui raízes reais

    # Calcula as raízes
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    return x1, x2

# Solicita os coeficientes da equação ao usuário
a = float(input("Digite o coeficiente 'a' da equação quadrática: "))
b = float(input("Digite o coeficiente 'b' da equação quadrática: "))
c = float(input("Digite o coeficiente 'c' da equação quadrática: "))

# Calcula as raízes da equação
raizes = calcular_raizes(a, b, c)

# Exibe o resultado
if raizes:
    print(f"Raízes da equação: {raizes}")
else:
    print("A equação não possui raízes reais.")
