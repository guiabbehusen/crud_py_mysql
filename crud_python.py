import mysql.connector

conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database='bdyoutube',

)

nome_produto = "toddynho"
valor = 10

cursor = conexao.cursor()

comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

cursor.execute(comando)
conexao.commit()


cursor.close()
conexao.close()