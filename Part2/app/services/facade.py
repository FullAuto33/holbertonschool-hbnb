from app.models.amenity import Amenity
from app.services.repository import InMemoryRepository  # Adapte selon ta couche repo

class HBnBFacade:
    def __init__(self):
        self.amenity_repo = InMemoryRepository()  # Exemple de repo

    def create_amenity(self, amenity_data):
        # Validation simple (ex: 'name' obligatoire)
        if not amenity_data.get('name'):
            raise ValueError("Amenity 'name' is required")
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.list_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if not amenity:
            return None
        # On met à jour uniquement les champs fournis
        if 'name' in amenity_data:
            amenity.name = amenity_data['name']
        self.amenity_repo.save(amenity)
        return amenity