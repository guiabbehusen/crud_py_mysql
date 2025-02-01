import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask
from models import db

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/to_do_list'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from views import *

if __name__ == "__main__":
        app.run()

