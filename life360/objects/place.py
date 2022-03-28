from .base import Base
from .user import User

class Place(Base):
    
    latitude, longitude, name, radius = int, int, str, int

    def __init__(self, access_token: str, **kwargs):
        super().__init__(access_token)
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.name = kwargs.get('name')
        self.radius = kwargs.get('radius')
        self.owner_id = kwargs.get('ownerId')
        self.circle_id = kwargs.get('circleId')
        
    def get_owner(self) -> User:
        """
        Returns the user that made the place.

        Returns
        -------
        User
            The owner of the place.
        """
        print("fir", (self.owner_id, self.circle_id))
        return User(self.access_token, (self.owner_id, self.circle_id))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'