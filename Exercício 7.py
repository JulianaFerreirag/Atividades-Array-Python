#Exercício 07 Faça um código para ler 5 números e armazenar em um vetor. Após a leitura total dos 5 números,
# o código deve escrever esses 5 números lidos na ordem inversa#

numeros = []

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("Números lidos na ordem inversa:")
for y in range(4, -1, -1):
    print(numeros[y])
