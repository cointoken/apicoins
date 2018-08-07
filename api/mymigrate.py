from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from datetime import datetime
from db.models import Coins
import config
import api.coins.passphrase

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =  True
db = SQLAlchemy(app)
migrate =  Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    c = Coins('eth','0xA71C99f3DCE29e7F0f64c284810FCFbDD3e39617',passphrase.generate(7),datetime.now())
    db.session.add(c)
    db.session.commit()
    manager.run()

