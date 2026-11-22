# Exercício complementar: comparação entre recursividade e repetição.
# Use números inteiros não negativos pequenos, como os exemplos abaixo.
def fatorial_recursivo(n):
    # Caso base: interrompe as chamadas recursivas.
    if n == 0:
        return 1
    return n * fatorial_recursivo(n - 1)


def fatorial_com_laco(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado


for numero in [0, 1, 4, 5]:
    print(
        numero,
        fatorial_recursivo(numero),
        fatorial_com_laco(numero)
    )
