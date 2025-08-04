from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity

def test_user_creation():
    user = User("Djelloul", "Rouba", "djelloulrouba@yahoo.com")
    print("User created:", user.first_name, user.email)

def test_place_with_review():
    user = User("Samir", "Kasmi", "Samir@kasmi.com")
    place = Place("Test place", "Place", 85, 42.1, -1.1, user)
    review = Review("Clean", 4, place, user)
    place.add_review(review)
    print("Place:", place.title, "has", len(place.reviews), "review(s)")

def test_amenity_creation():
    amenity = Amenity("Wi-Fi")
    print("Amenity:", amenity.name)

if __name__ == "__main__":
    test_user_creation()
    test_place_with_review()
    test_amenity_creation()
