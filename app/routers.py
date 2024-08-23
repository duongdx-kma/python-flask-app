from flask import render_template, request, redirect, url_for, current_app as app
from .logic import get_users, add_user_to_db

@app.route('/')
def index():
    users = get_users()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user_to_db(name, email)
        return redirect(url_for('index'))
    return render_template('add_user.html')
