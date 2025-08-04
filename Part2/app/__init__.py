# Importation des modules nécessaires
from flask import Flask  # Importe la classe Flask du module flask
from flask_restx import Api  # Importe la classe Api du module flask_restx

# Fonction de création de l'application Flask
def create_app():
    # Création d'une instance de l'application Flask
    app = Flask(__name__)
    
    # Création d'une instance de l'API REST avec Flask-RESTX
    api = Api(
        app,  # L'application Flask à laquelle l'API est attachée
        version='1.0',  # Version de l'API
        title='HBnB API',  # Titre de l'API
        description='HBnB Application API',  # Description de l'API
        doc='/api/v1/'  # Chemin de la documentation Swagger UI
    )

    # Les endpoints de l'API seront ajoutés plus tard

    # Retourne l'application Flask configurée
    return app
