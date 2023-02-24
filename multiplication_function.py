def multiplicacao(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado

total_multiplicacao = multiplicacao(4, 8)
print(total_multiplicacao)
