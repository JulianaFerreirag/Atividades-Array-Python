#Faça um código para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois
#vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos
#elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o
#vetor Soma#


def ler_vetor(N):
    vetor = []
    for i in range(N):
        elemento = float(input(f"Digite o elemento {i + 1} do vetor: "))
        vetor.append(elemento)
    return vetor

def soma_vetores(A, B):
    soma = []
    for j in range(len(A)):
        soma.append(A[j] + B[j])
    return soma


def main():
    N = int(input("Digite o tamanho dos vetores (N): "))

    print("Digite os elementos do vetor A:")
    vetor_A = ler_vetor(N)

    print("Digite os elementos do vetor B:")
    vetor_B = ler_vetor(N)

    vetor_Soma = soma_vetores(vetor_A, vetor_B)

    print("Vetor Soma:", vetor_Soma)


if __name__ == "__main__":
    main()
