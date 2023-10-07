#3 Altere o exercício anterior para permitur achar o nome de um aluno na lista.

Contador = 0
Quant_Alu = int(input("Digite a quantidade de alunos da sala :"))
Nome_Alu = [0] * Quant_Alu
for x in range(Quant_Alu):
    Nome_Alu[x] = input("Nome do Aluno: ")  # preencheu meu array

for y in range(Quant_Alu):  # no for variavel y para não confudir com o primeiro for x
    print(f"{Nome_Alu[y]} está na posição {y}")

Pesquisa = input("Digite o nome de um aluno para verificar se ele está presente na sala: ")
for j in range (Quant_Alu):
    if Nome_Alu[j] == Pesquisa :
        print(f"{Pesquisa} está na lista, na posição {j}")
        Contador = Contador + 1
if Contador == 0:
        print(f"O nome {Pesquisa} não está na lista!!!!")
