

numeros = [10, -7, 24, -2, 8, 15, -10, 0, 7, 12, -23, 45, -1, 99, -50, 100, -75, 25, -100, 50, -25, 75, -12, 23, -15, 10, -8, 24, -36]
print("vetores", numeros)
referencia_maior = numeros[15]
referencia_menor = numeros[18]
print("O maior número é: ", referencia_maior)
print("O menor número é: ", referencia_menor)

soma_numeros_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_numeros_pares += numero

print("A soma dos números pares é: ", soma_numeros_pares)

soma_numeros_impares = 0

for numero in numeros:
    if numero % 2 != 0:
        soma_numeros_impares += numero 

print("A soma dos números ímpares é: ", soma_numeros_impares)
