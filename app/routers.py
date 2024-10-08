from flask import render_template, request, redirect, url_for
from app import db  # Import db instance
from app.logic import get_users, add_user_to_db  # Import logic functions

def register_routes(app):
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
