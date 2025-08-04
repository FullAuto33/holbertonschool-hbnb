# Importation des modules nécessaires
import uuid  # Pour générer des identifiants uniques
from datetime import datetime  # Pour travailler avec des dates et heures

# Classe de base pour les modèles qui partagent des attributs communs
class BaseModel:
    def __init__(self):
        # Génération d'un identifiant unique pour chaque instance
        self.id = str(uuid.uuid4())
        
        # Initialisation de la date de création et de la date de dernière mise à jour
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    # Méthode pour enregistrer et mettre à jour la date de dernière modification
    def save(self):
        """Met à jour la date de modification"""
        self.updated_at = datetime.now()  # Met à jour l'attribut 'updated_at' avec l'heure actuelle

    # Méthode pour mettre à jour les attributs de l'objet à partir d'un dictionnaire
    def update(self, data: dict):
        """Met à jour les attributs valides à partir d'un dictionnaire"""
        # Parcours des paires clé/valeur du dictionnaire
        for key, value in data.items():
            # Si l'objet possède l'attribut correspondant à la clé, on met à jour sa valeur
            if hasattr(self, key):
                setattr(self, key, value)
        
        # Après avoir mis à jour les attributs, on enregistre l'objet (en mettant à jour la date de modification)
        self.save()
