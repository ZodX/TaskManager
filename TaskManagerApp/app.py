from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///test.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feladat = db.Column(db.String(200), nullable=False)
    csoport = db.Column(db.String(100))
    prioritas = db.Column(db.Integer, default=5)
    datum = db.Column(db.DateTime, default=datetime.utcnow)
    kesz = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('feladatok.html')

if __name__ == '__main__':
    app.run(debug = True)