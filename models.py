from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# User Model
class User(UserMixin):
    def __init__(self, username, password, role):
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
