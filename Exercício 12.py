'''Exercício 12 Escreva um algoritmo que solicite ao usuário a entrada de 5 nomes, e que exiba
a lista desses nomes na tela. Após exibir essa lista, o programa deve mostrar também os nomes
na ordem inversa em que o usuário os digitou, um por linha '''


def ler_nomes():
    nomes = []
    for i in range(5):
        nome = input(f"Digite o {i + 1}º nome: ")
        nomes.append(nome)
    return nomes


def main():
    nomes = ler_nomes()

    print("\nNomes digitados:")
    for nome in nomes:
        print(nome)

    print("\nNomes na ordem inversa:")
    for nome in reversed(nomes):
        print(nome)


if __name__ == "__main__":
    main()
print( )
print("Programa encerrado, até breve!")