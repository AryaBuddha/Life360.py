from tokenize import Double
from .base import Base

class User(Base):
    first_name, last_name, email, avatar, phone, created_at = str, str, str, str, str, str
    latitude, longitude, at_since, location, battery, is_driving = float, float, int, str, int, bool


    def __init__(self, access_token: str, circle_id: str, user_id: str):
        super().__init__(access_token)
        self.circle_id = circle_id
        self.id = user_id

        r = self.get(f'/circles/{circle_id}/members/{self.id}')

        location = r['location']

        self.latitude = float(location['latitude'])
        self.longitude = float(location['longitude'])
        self.at_since = location['since']
        self.location = location['name'] if location['name'] != None else f'{location["address1"]} {location["address2"]}'
        self.battery = int(location['battery'])
        self.is_driving = False if int(location['isDriving']) == 0 else True

        self.first_name = r['firstName']
        self.last_name = r['lastName']
        self.email = r['loginEmail']
        self.avatar = r['avatar']
        self.phone = r['loginPhone']
        self.created_at = r['createdAt']
    

    def get_trips(self):
        r = self.get(f'/circles/{self.circle_id}/users/{self.id}/driverbehavior/trips')
        return r
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'