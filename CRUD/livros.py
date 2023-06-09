import conexao as conn

Opcao = 0

while(True):
    Opcao = input("Digite uma opção \n 1 - Cadastar um novo livro \n 2 - Listar todos os livros \n 3- Sair \n")
    match Opcao:
        case "1":
            nome = input("Digite o nome do livro: ")
            codBarras = input("Digite o código de barras de 11 dígitos: ")
            autor = input("Digite o autor: ")

            comando  =f"""INSERT INTO Livros (nome, codBarras, Autor) VALUES('{nome}', '{codBarras}', '{autor}')"""
            conn.cursor.execute(comando)
            conn.cursor.commit()
            print("Cadastro realizado com sucesso!")
        case "2":
            comando = """SELECT * FROM Livros"""
            result = conn.cursor.execute(comando)
            for row in result:
                print(row)
        case "3":
            break

