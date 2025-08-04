# Importation de la classe de base `BaseModel` pour bénéficier des attributs et méthodes communs
from app.models.base_model import BaseModel

# Classe représentant un lieu (Place), héritant de `BaseModel`
class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        # Appel du constructeur de la classe de base pour initialiser les attributs communs
        super().__init__()

        # Validation du titre : il doit être non vide et avoir une longueur maximale de 100 caractères
        if not title or len(title) > 100:
            raise ValueError("Title is required and must be 100 characters or fewer.")
        
        # Validation du prix : il doit être positif
        if price <= 0:
            raise ValueError("Price must be a positive value.")
        
        # Validation de la latitude : elle doit être comprise entre -90 et 90
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Latitude must be between -90 and 90.")
        
        # Validation de la longitude : elle doit être comprise entre -180 et 180
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Longitude must be between -180 and 180.")
        
        # Validation du propriétaire : il doit être fourni (ici, un utilisateur)
        if not owner:
            raise ValueError("Owner (User) is required.")

        # Initialisation des attributs spécifiques à la classe `Place`
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner  # Propriétaire du lieu (instance de la classe `User`)
        
        # Initialisation des attributs pour les avis et les commodités (vide par défaut)
        self.reviews = []  # Liste des avis pour ce lieu
        self.amenities = []  # Liste des commodités pour ce lieu

    # Méthode pour ajouter un avis à un lieu
    def add_review(self, review):
        self.reviews.append(review)  # Ajoute l'avis à la liste des avis

    # Méthode pour ajouter une commodité à un lieu
    def add_amenity(self, amenity):
        self.amenities.append(amenity)  # Ajoute la commodité à la liste des commodités
