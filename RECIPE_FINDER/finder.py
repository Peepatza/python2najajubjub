from api_comm import ApiChecker
from display import RecipeDisplay


class RecipeFinder:
    
    def __init__(self, setting):
        self.api = ApiChecker(setting.api_key, setting.url)
        self.display = RecipeDisplay()

    def search(self, ingredient, count=5):
        print(f"\nSearching for recipes with: {ingredient}")
        return self.api.get_recipes(ingredient, count)