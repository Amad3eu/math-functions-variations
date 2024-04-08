# Variações da utilizações de funções matemáticas
- Respondido na atividade proposta por meio de um um forum
- Foi desenvolvido dois seguintes exemplos:

1. **Fatorial:**
A função math.factorial() é utilizada para calcular o fatorial de um número. Neste código, o usuário digita um número inteiro positivo, e a função math.factorial() é aplicada a esse número para calcular o fatorial.

```python
import math

def calcular_fatorial(n):
return math.factorial(n)

# Exemplo de uso
resultado = calcular_fatorial(5)
print(resultado) # Saída: 120
```

---

2. **Bhaskara:**
No código do Bhaskara, são utilizadas as funções math.sqrt() para calcular a raiz quadrada e math.pow() para elevar um número à potência. A raiz quadrada é utilizada para calcular a raiz quadrada do discriminante, e a potência é usada para elevar o coeficiente 'b' ao quadrado. Essas operações são parte do cálculo das raízes da equação quadrática através da fórmula de Bhaskara.

```python
import math

def calcular_raizes(a, b, c):
# Calcula o discriminante
delta = b**2 - 4*a*c

# Verifica se a equação tem raízes reais
if delta < 0:
return None # Equação não possui raízes reais

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
07/04/2024 às 23:53
``
