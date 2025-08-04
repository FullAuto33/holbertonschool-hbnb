from app import bcrypt
from uuid import uuid4

class User:
    def __init__(self, first_name, last_name, email, password=None, is_admin=False):
        self.id = str(uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = None
        if password:
            self.hash_password(password)
        self.is_admin = is_admin

    def hash_password(self, password):
        """Hash le mot de passe avec bcrypt"""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Vérifie le mot de passe (utilisé plus tard dans le login)"""
        return bcrypt.check_password_hash(self.password, password)

    def to_dict(self):
        """Retourne un dictionnaire sans le mot de passe"""
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }
