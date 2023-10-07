#Ler 5 um vetor A de 10 números. logo em seguida, ler mais um número e guardar em
#uma variável X. Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo
#valor X. Logo após, imprimir o vetor M#



Notas = [0]*5  #Criou o array
contAlunos = 0
Soma = 0
for x in range (5):
    Notas [x] = float(input("Informa a nota: "))

for y in range (5) :
    Soma+=Notas[y]

media = Soma/5

for z in range (5):
     if  Notas[z]>=media:
        contAlunos+=1

print(f"A média da sala é {media} e {contAlunos} Obtiveram  notas acima da média. ")
