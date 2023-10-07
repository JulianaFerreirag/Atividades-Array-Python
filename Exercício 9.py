#Exercício 09 Altere o sistema anterior e faça um sistema de login, pedindo a senha do usuário e
#mostrando seu nome e a mensagem, login efetuado com sucesso.

nomes_usuarios = []
senhas = []

for i in range(5):
    nome = input(f"Digite o nome do usuário {i + 1}: ")
    senha = input(f"Digite a senha do usuário {i + 1}: ")

    nomes_usuarios.append(nome)
    senhas.append(senha)

senha_login = input("Digite sua senha para fazer login: ")

login_efetuado = False
for y in range(5):
    if senha_login == senhas[y]:
        print(f"Login efetuado com sucesso! Bem-vindo, {nomes_usuarios[y]}")
        login_efetuado = True
        break

if not login_efetuado:
    print("Senha incorreta. O login não foi efetuado.")
