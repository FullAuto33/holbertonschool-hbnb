# Importation de la classe de base `BaseModel` pour étendre ses fonctionnalités
from app.models.base_model import BaseModel

# Classe représentant un utilisateur, héritant de `BaseModel`
class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        # Appel du constructeur de la classe de base pour initialiser les attributs communs
        super().__init__()

        # Validation du prénom : il doit être non vide et avoir une longueur maximale de 50 caractères
        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and must be 50 characters or fewer.")
        
        # Validation du nom de famille : il doit être non vide et avoir une longueur maximale de 50 caractères
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and must be 50 characters or fewer.")
        
        # Validation de l'email : il doit être non vide et contenir un '@'
        if not email or '@' not in email:
            raise ValueError("Valid email is required.")

        # Initialisation des attributs spécifiques à la classe `User`
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin  # Par défaut, un utilisateur n'est pas administrateur

        def update(self, data):
            for key, value in data.items():
                if hasattr(self, key):
                    setattr(self, key, value)
            self.updated_at = datetime.now()
