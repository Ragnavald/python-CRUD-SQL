import conexao as conn

while(True):
    Opcao = input("Selecione a opção \n 1 - Cadastrar novos clientes \n 2 - Listar todos os clientes \n 3 - Sair \n")
    match Opcao:
        case "1":
            nome = input("Digite o nome do cliente: ")
            idade = input("Digite a idade do cliente: ")
            cpf = input("Digite o CPF: ")

            comando = f"""INSERT INTO Clientes(nome,idade,cpf) VALUES('{nome}', {idade}, '{cpf}')"""
            conn.cursor.execute(comando)
            conn.cursor.commit()
        case "2":
            result = conn.cursor.execute("""SELECT * FROM Clientes""")
            for row in result:
                print(row)
        case "3":
            break