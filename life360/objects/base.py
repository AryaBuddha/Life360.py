import requests

class Base():

    def __init__(self, access_token: str):
        self.access_token = access_token

    def get(self, path: str) -> dict:
        """
        Returns a list of objects from the specified path.
        
        Parameters
        ----------
        path : str
            The path to the objects.
        
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