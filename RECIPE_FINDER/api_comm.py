import requests


class ApiChecker:
    
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url

    def get_recipes(self, ingredient, count=5):
        params = {
            "apiKey": self.api_key,
            "ingredients": ingredient,
            "number": count,
            "ignorePantry": True
        }
        
        try:
            response = requests.get(self.url, params=params, timeout=69)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print("Error: your internet might be bad bro")
        except requests.exceptions.ConnectionError:
            print("Error: connect to internet bro")
        return None