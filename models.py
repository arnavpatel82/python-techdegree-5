from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Project Title', db.String())
    date = db.Column('Completion Date', db.DateTime, default=datetime.datetime.now)
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.String())

    def __repr__(self):
        return f"""<Project (Project Title: {self.title}
                Completion Date: {self.date}
                Description: {self.description}
                Skills: {self.skills}
                )>"""