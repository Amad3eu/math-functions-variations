import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi**n - (-phi)**(-n)) / math.sqrt(5))

# Exemplo de uso
resultado = fibonacci(10)
print(resultado)  # Saída: 55
