import mysql.connector

    # Conectar ao banco de dados
conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='bdyoutube'
    )

cursor = conexao.cursor()

nome_produto = "nescau"
valor = 3
comando = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}', {valor})"
print


cursor.execute(comando)
conexao.commit()




cursor.close()
conexao.close()

