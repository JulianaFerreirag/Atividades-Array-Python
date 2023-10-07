#1 Perguntar ao usuário quantos alunos tem na sala e criar um array,
#unidimensurável(vetor) com o nome de todos os alunos da sala.

Quant_Alu = int(input("Digite a quantidade de alunos da sala :"))
Nome_Alu = [0]*Quant_Alu
for x in range (Quant_Alu) :
    Nome_Alu[x] = input("Nome do Aluno: ") #preencheu meu array
for y in range (Quant_Alu):  #no for variavel y para não confudir com o primeiro for x
    print(Nome_Alu[y], end=" ") #print leu array


