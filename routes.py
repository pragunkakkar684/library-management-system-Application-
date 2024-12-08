# routes.py

from flask import Flask, request, url_for, render_template, flash, redirect, Blueprint
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import User

routes = Blueprint('routes', __name__)

app = Flask(__name__)
app.secret_key = "12345"

login_manager = LoginManager(app)
login_manager.login_view = "routes.login"

# Dummy User Database
users = {
    "admin": User("admin", "adminpass", "admin"),
    "librarian": User("librarian", "libpass", "employee"),
    "member": User("member", "mempass", "member")
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Login route
@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        u = users.get(username)

        if u and u.check_password(password):
            login_user(u)
            flash('Logged in successfully', 'success')
            return redirect(url_for('routes.dashboard'))
        else:
            flash('Invalid login credentials', 'danger')

    return render_template('login.html')

# Logout route
@routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out', 'info')
    return redirect(url_for('routes.login'))

# Dashboard route
@routes.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome {current_user.username}! Role: {current_user.role}'
