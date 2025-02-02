from crud_python import app
from flask import render_template, request, redirect, url_for
from models import *
import datetime

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/create_task", methods=['GET', 'POST'])
def create_task():
    today = datetime.date.today()
    if request.method == 'POST':
        descricao = request.form['descricao']
        data_criacao = request.form.get('data_criacao')
        if not data_criacao:
            data_criacao = today
        else:
            try:
                data_criacao = datetime.datetime.strptime(data_criacao, "%Y-%m-%d").date()
            except ValueError:
                data_criacao = today

        data_conclusao = request.form.get('data_conclusao')
        if data_conclusao:
            try:
                data_conclusao = datetime.datetime.strptime(data_conclusao, "%Y-%m-%d").date()
            except ValueError:
                data_conclusao = None
        else:
            data_conclusao = None

        status = int(request.form.get('status', 0))
        
        if not descricao:
            return "Erro: Descrição é obrigatória", 400

        nova_tarefa = Tarefas(
            descricao=descricao,
            status=status,
            data_criacao=data_criacao,
            data_conclusao=data_conclusao,
        )

        try:
            db.session.add(nova_tarefa)
            db.session.commit()
            return redirect(url_for("view_tasks"))
        except Exception as e:
            db.session.rollback()
            return f"Erro ao salvar tarefa: {str(e)}", 500
    
    return render_template('create_task.html', today=today)


@app.route("/view_tasks")
def view_tasks():
    tasks = Tarefas.query.all()  
    return render_template('view_tasks.html', tasks=tasks) 

@app.route('/view_in_progress')
def in_progress():
    tasks_in_progress = Tarefas.query.filter_by(status=0).all() 
    return render_template('view_in_progress.html', tasks=tasks_in_progress)

@app.route("/view_completed")
def completed():
    tasks_completed = Tarefas.query.filter_by(status=1).all() 
    return render_template('view_completed.html', tasks=tasks_completed)

@app.route("/edit_tasks/<int:idtarefas>", methods=['GET', 'POST'])
def edit_task(idtarefas):
    task = Tarefas.query.get_or_404(idtarefas)
    if request.method == 'POST':
        task.descricao = request.form.get('descricao', task.descricao)
        task.status = int(request.form.get('status', task.status))
        data_criacao = request.form.get('data_criacao')
        if data_criacao:
            task.data_criacao = datetime.datetime.strptime(data_criacao, "%Y-%m-%d").date()

        data_conclusao = request.form.get('data_conclusao')
        if data_conclusao:
            task.data_conclusao = datetime.datetime.strptime(data_conclusao, "%Y-%m-%d").date()
        else:
            task.data_conclusao = None
        db.session.commit()
        return redirect(url_for("view_tasks"))
    return render_template("edit_tasks.html", task=task)
