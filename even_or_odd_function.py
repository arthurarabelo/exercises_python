def par(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é ímpar'

par_impar = par(60)
print(par_impar)
