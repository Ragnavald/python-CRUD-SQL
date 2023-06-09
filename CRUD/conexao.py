import pyodbc

dados_conexao = (
    "Driver={SQL SERVER};"
    "Server=DESKTOP-8IVDFIR;"
    "Database=Test;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()


