from .base import Base
from .user import User
from .place import Place

class Circle(Base):
    """
    Represents a circle from the point of view of the current user.
    """


    name, color, created_at, member_count = str, str, str, int    

    def __init__(self, access_token: str, **kwargs):
        super().__init__(access_token)
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.color = kwargs.get('color')
        self.created_at = kwargs.get('createdAt')
        self.member_count = kwargs.get('memberCount')

    def get_members(self) -> list:
        """
        Returns a list of users associated with the circle.

        Returns
        -------
        list
            A list of :class:`User` objects.
        """
        r = self.get(f'/circles/{self.id}/members')
        return [User(self.access_token, self.id, m['id']) for m in r['members']]
        

    def get_places(self) -> list:
        """
        Returns a list of places associated with the circle.

        Returns
        -------
        list
            A list of :class:`Place` objects.
        """
        r = self.get(f'/circles/{self.id}/allplaces')
        return [Place(self.access_token, **p) for p in r['places']]
        

    def __str__(self):
        return f'{self.name}'