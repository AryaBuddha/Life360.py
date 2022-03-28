import requests
import json

from .objects import (
    User,
    Circle
)

class Life360Client:

    __all__ = ["get_user", "get_circles", "check"]
    """
    Represents a connection to the Life360 API. 
    
    :class:`Client` supports a variety of options and methods to interact with the API.
    """

    def __init__(self, access_token: str, user: dict):
        self.access_token = access_token
        self.user_first = user['firstName']
        self.user_last = user['lastName']

    @staticmethod
    def login(username: str, password: str) -> User:
        """
        Initate a login session with the Life360 API.

        Parameters
        ----------
        username : str
            The username of the account. Could be the email or phone number.
        password : str
            The password of the account.

        Returns
        -------
        Life360Client
            A :class:`Life360Client` object representing session with Life360.

        """
        r = requests.post(
            "https://api-cloudfront.life360.com/v3/oauth2/token",
            headers={
                'Authorization': 'Basic YnJ1czR0ZXZhcHV0UmVadWNydUJSVXdVYnJFTUVDN1VYZTJlUEhhYjpSdUt1cHJBQ3JhbWVzV1UydVRyZVF1bXVtYTdhemFtQQ==',
                'User-Agent': 'SafetyMapKoko/22.2.0.487/CBC47A39-34C3-43F2-9924-E7F1F928AC1C',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            data = json.dumps({
                "grant_type": 'password',
                "username": username,
                "password": password 
            })
        )
        r = r.json()
        return Life360Client(r['access_token'], r['user'])


    #def get_user(self) -> User:
        """
        Returns the user object of the current session.

        Returns
        -------
        User
            A :class:`User` object representing the user account.
        """
        return self.user


    def get_circles(self) -> list:
        """
        Returns a list of circles associated with the user.

        Returns
        -------
        list
            A list of :class:`Circle` objects.
        """
        r = self.__get_path("/circles")
        return [Circle(self.access_token, **c) for c in r['circles']]



    def __get_path(self, path: str) -> dict:
        """
        Returns a list of objects from the specified path.

        Parameters
        ----------
        path : str
            The Life360 API path to retrieve.

        Returns
        -------
        dict
            A dictionary of returned information.
        """
        r = requests.get(
            "https://api-cloudfront.life360.com/v3" + path,
            headers={
                'Authorization': 'Bearer ' + self.access_token,
            },
        )
        return r.json()

    

    def check(self):
        """
        Checks to see if the function worked
        Just prints our your ``name`` to make sure that it
        
        """
        print("worked")
