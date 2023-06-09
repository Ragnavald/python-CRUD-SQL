import conexao as conn
from datetime import datetime, timedelta 
Opcao = 0

while(True):
    Opcao = input("\n Selecione uma opção: \n 1 - Cadastrar empréstimo \n 2 - Listar empréstimos \n 3 - Verificar clientes em atraso \n 4 - Sair \n")
    match Opcao:
        case "1":
            now = datetime.today()
            Idcliente = input("Digite o Id do cliente: ")
            IdLivro =  input("Digite o Id do Livro: ")
            DataVencimento = now +timedelta(days = 15)

            comando = f"""INSERT INTO Emprestimos (FKCliente, FKLivro, DataEmprestimo, DataRecebida, DataVencimento) VALUES
            ({Idcliente},{IdLivro},'{now}',NULL, '{DataVencimento}')"""

            conn.cursor.execute(comando)
            conn.cursor.commit()
        case "2":
            comando = """ SELECT cli.nome as 'Cliente', li.nome as 'Livro', emp.DataEmprestimo as 'Data de Empréstimo', emp.DataRecebida as 'Data Recebida', emp.DataVencimento as 'Data do Vencimento' FROM Emprestimos as emp  JOIN Clientes as cli ON emp.FKCliente = cli.IdCliente  JOIN
Livros as li ON emp.FKLivro = li.IdLivro"""
            result = conn.cursor.execute(comando)
            for row in result:
                print(row)

        case "3":
            comando = """ SELECT cli.nome as 'Cliente', li.nome as 'Livro', emp.DataEmprestimo as 'Data de Empréstimo', emp.DataRecebida as 'Data Recebida', emp.DataVencimento as 'Data do Vencimento' FROM Emprestimos as emp  JOIN Clientes as cli ON emp.FKCliente = cli.IdCliente  JOIN
Livros as li ON emp.FKLivro = li.IdLivro WHERE emp.DataRecebida IS NULL and emp.DataVencimento < CONVERT(VARCHAR(10), getdate(), 23);"""
            result = conn.cursor.execute(comando)
            
            for row in result:
                print(row)
        case "4":
            break