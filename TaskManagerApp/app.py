from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

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

@app.route('/', methods=['POST','GET'])
def index():
    if request.method =='POST':

        task_feladat = request.form['Feladat']
        task_csoport = request.form['Csoport']
        task_prioritas = request.form['Prioritas']
        
        uj_task = Task(feladat=task_feladat,csoport=task_csoport,prioritas=task_prioritas)

        try:
            db.session.add(uj_task)
            db.session.commit()
            return redirect('/')
        except:
            return "Hiba történt a feladat hozzáadása közben!"

    else:
        feladatok = Task.query.order_by(desc(Task.datum)).all()
        return render_template('feladatok.html', feladatok=feladatok)


if __name__ == '__main__':
    app.run(debug = True)