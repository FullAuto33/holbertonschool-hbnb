from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, place, user):
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
	
    @property
    def text(self):
        return self.__text
	
    @text.setter
    def text(self, value):
        if not value:
            raise ValueError("Text no empty")
        if not isinstance(value, str):
            raise TypeError("Text string")
        self.__text = value

    @property
	def rating(self):
	    return self.__rating
	
	@rating.setter
	def rating(self, value):
		if not isinstance(value, int):
			raise TypeError("Rating integer")
		super().is_between('Rating', value, 1, 6)
		self.__rating = value

	@property
	def place(self):
		return self.__place
	
	@place.setter
	def place(self, value):
		if not isinstance(value, Place):
			raise TypeError("Place instance")
		self.__place = value

	@property
	def user(self):
		return self.__user
	
	@user.setter
	def user(self, value):
		if not isinstance(value, User):
			raise TypeError("User  instance")
		self.__user = value

	def to_dict(self):
		return {
			'id': self.id,
			'text': self.text,
			'rating': self.rating,
			'place_id': self.place.id,
			'user_id': self.user.id
		}
