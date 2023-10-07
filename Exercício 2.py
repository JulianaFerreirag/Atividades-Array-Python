#2 Altere o exer´cicio anterior e mostre na tela, ao final, on ome de cada aluno e sua respectiva
#posição no array.

Quant_Alu = int(input("Digite a quantidade de alunos da sala :"))
Nome_Alu = [0]*Quant_Alu
for x in range (Quant_Alu) :
    Nome_Alu[x] = input("Nome do Aluno: ") #preencheu meu array
for y in range (Quant_Alu):  #no for variavel y para não confudir com o primeiro for x
    print(f"{Nome_Alu[y]} está na posição {y}")