# Importation de la classe de base `BaseModel` pour bénéficier des attributs et méthodes communs
from app.models.base_model import BaseModel

# Classe représentant un lieu (Place), héritant de `BaseModel`
class Place(BaseModel):
    # Attributs ...

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be non-negative")
        self._price = value

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if value < -90 or value > 90:
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = value

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if value < -180 or value > 180:
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = value
