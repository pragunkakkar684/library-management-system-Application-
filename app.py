from flask import Flask, render_template
from routes import routes  # Import the Blueprint for routes
from flask_login import LoginManager
from models import User

# Create Flask app instance
app = Flask(__name__)
app.secret_key = "12345"  # Required for session management

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login'  # Specify the login view route

# Register the Blueprint
app.register_blueprint(routes)

users = {
    "admin": User("admin", "adminpass", "admin"),
    "librarian": User("librarian", "libpass", "employee"),
    "member": User("member", "mempass", "member")
}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Define home route (optional)
@app.route('/')
def home():
    return 'Welcome to the Library Management System'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
