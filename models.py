import datetime
import mysql.connector
from flask import Flask, app, SQLAlchemy

conexao = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="123456",
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@127.0.0.1/to_do_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tarefas(db.Model):
    __tablename__= 'tarefas'
    idtarefas = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, default=0)
    data_criacao = db.Column(db.Date, default=datetime.date.today)
    data_conclusao = db.Column(db.Date, nullable=True)

if __name__ == "__main__":
    app.run(debug=True)