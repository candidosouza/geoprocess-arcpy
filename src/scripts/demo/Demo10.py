import random
totalpares = 0
totalimpar = 0
pares = []
impares = []

for c in range(0, 50):
    n = random.randint(1, 101)
    if n % 2 == 0:
        totalpares = totalpares + 1
        pares.append(n)
    elif n % 2 == 1:
        totalimpar += 1
        impares.append(n)
print(f'Total de  números pares: {totalpares}\nTotal de números ímpares: {totalimpar}')
print(f'Lista de números pares sorteados: {pares}\nLista de números impares sorteados: {impares}')