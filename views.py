from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from model import person, User


def register_views(app, db):
    @app.route('/', methods=["GET", "POST"])
    def index():
        if request.method == 'GET':
            people = person.query.all()
            print(type(person.pid))
            return render_template('db.html', person=people)
        elif request.method == 'POST':
            name = request.form['name']
            age = int(request.form['age'])
            job = request.form['job']

            pers = person(name=name, age=age, job=job)

            db.session.add(pers)
            db.session.commit()

            people = person.query.all()
            return render_template('db.html', person=people)
    
    @app.route('/delete/<pid>', methods=["DELETE"])
    def delete(pid):
        person.query.filter(person.pid == pid).delete()
        db.session.commit()
        pers = person.query.all()
        return render_template("db.html", person=pers)

def login_page(app, db, bcrypt):
    @app.route('/')
    def index():
        return render_template('Home_page.html')
    
    @app.route('/signup', methods=["GET", "POST"])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            hashed_password = bcrypt.generate_password_hash(password)

            user = User(username=username, pasword=hashed_password)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))
    
    @app.route('/login', methods=["GET", "POST"])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter(User.username == username).first()

            if bcrypt.check_password_hash(user.pasword, password):
                login_user(user=user)
                return render_template('Home_page.html')
            else:
                return "Failed"
    
    @app.route('/logout')
    def logout():
        logout_user()
        return render_template('Home_page.html')