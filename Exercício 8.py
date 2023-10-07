#Exercício 08 Faça um código para ler 5 nomes de usuários e suas respectivas senhas,
#e armazenar cada lista em um array diferente, após completar a digitação, imprimir ,
#nome, senha e posição dos dados no array


nomes = []
senhas = []

for x in range(5):
    nome = input(f"Digite o nome do usuário {x + 1}: ")
    senha = input(f"Digite a senha do usuário {x + 1}: ")

    nomes.append(nome)
    senhas.append(senha)
print("\nNomes e Senhas Armazenados:")

for x, (nome, senha) in enumerate(zip(nomes, senhas)):
    print(f"Posição {x + 1} - Nome: {nome}, Senha: {senha}")
