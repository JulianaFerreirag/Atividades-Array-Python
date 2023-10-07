#4 Perguntar ao usuário se ainda tem alguma pesquisa.Utilizando o código anterior

Nova_Pesquisa = "s"
while Nova_Pesquisa "Ss"

Contador = 0
Quant_Alu = int(input("Digite a quantidade de alunos da sala :"))
Nome_Alu = [0] * Quant_Alu
for x in range(Quant_Alu):
    Nome_Alu[x] = input("Nome do Aluno: ")  # preencheu meu array

for y in range(Quant_Alu):  # no for variavel y para não confudir com o primeiro for x
    print(f"{Nome_Alu[y]} está na posição {y}")

while Nova_Pesquisa == 'S'
    Contador = 0
    Pesquisa = input("Digite o nome de um aluno para verificar se ele está presente na sala: ")
    for j in range (Quant_Alu):
        if Nome_Alu[j] == Pesquisa :
            print(f"{Pesquisa} está na lista, na posição {j}")
            Contador = Contador + 1
    if Contador == 0:
            print(f"O nome {Pesquisa} não está na lista!!!!")
    Nova_Pesquisa = input("Deseja pesquisar outro nome? ")
