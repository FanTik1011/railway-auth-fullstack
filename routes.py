from flask import render_template, redirect, url_for, request
from app import app, db
from models import User
from flask_login import login_user, logout_user, login_required

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return "Login logic here"

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
