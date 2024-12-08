from flask import Flask,request,url_for,render_template,flash,redirect
from flask_login import LoginManager,login_user,logout_user,login_required,current_user

app = Flask(__name__)
app.secret_key = "12345"

login_manager = LoginManager(app)
login_manager.login_view='login'

# Dummy User Database
users = {
    "admin": User("admin", "adminpass", "admin"),
    "librarian": User("librarian", "libpass", "employee"),
    "member": User("member", "mempass", "member")
}

@login_manager.user_loader
def load_user(username):
    return users.get(username)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user.check_password(password):
            login_user(user)
            flash("Logged in succesfully",'success')
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid user name or password!",'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    login_user()
    flash('You have been loged out','info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return f'Welcome {current_user.username}! Role: {current_user.role}'


