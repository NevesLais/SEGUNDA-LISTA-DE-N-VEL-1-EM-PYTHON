
usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")


if usuario == "admin" and senha == "123":
    print("Usuário logado com sucesso!")
else:
    if usuario != "admin" and senha != "123":
        print("Usuário e senha incorretos.")
    elif usuario != "admin":
        print("Usuário incorreto.")
    elif senha != "123":
        print("Senha incorreta.")
