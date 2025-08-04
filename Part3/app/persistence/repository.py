# Importation du module ABC pour créer des classes abstraites
from abc import ABC, abstractmethod

# Définition d'une interface Repository en tant que classe abstraite
class Repository(ABC):
    # Méthode abstraite pour ajouter un objet
    @abstractmethod
    def add(self, obj): pass

    # Méthode abstraite pour récupérer un objet par son ID
    @abstractmethod
    def get(self, obj_id): pass

    # Méthode abstraite pour récupérer tous les objets
    @abstractmethod
    def get_all(self): pass

    # Méthode abstraite pour mettre à jour un objet en fonction de son ID
    @abstractmethod
    def update(self, obj_id, data): pass

    # Méthode abstraite pour supprimer un objet par son ID
    @abstractmethod
    def delete(self, obj_id): pass

    # Méthode abstraite pour récupérer un objet selon un attribut spécifique
    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value): pass


# Implémentation concrète de Repository utilisant un stockage en mémoire
class InMemoryRepository(Repository):
    def __init__(self):
        # Dictionnaire interne servant de stockage (clé = ID, valeur = objet)
        self._storage = {}

    # Ajoute un objet dans le stockage
    def add(self, obj):
        self._storage[obj.id] = obj

    # Récupère un objet à partir de son ID
    def get(self, obj_id):
        return self._storage.get(obj_id)

    # Récupère la liste de tous les objets
    def get_all(self):
        return list(self._storage.values())

    # Met à jour un objet existant avec de nouvelles données
    def update(self, obj_id, data):
        obj = self.get(obj_id)
        if obj:
            for key, value in data.items():
                setattr(obj, key, value)  # Met à jour les attributs de l'objet

    # Supprime un objet du stockage par son ID
    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]

    # Recherche un objet selon la valeur d'un de ses attributs
    def get_by_attribute(self, attr_name, attr_value):
        return next(
            (obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value),
            None  # Retourne None si aucun objet ne correspond
        )
