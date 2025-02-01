import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Tarefas(db.Model):
    __tablename__= 'tarefas'
    idtarefas = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Integer, default=0)
    data_criacao = db.Column(db.Date, default=datetime.date.today)
    data_conclusao = db.Column(db.Date, nullable=True)
