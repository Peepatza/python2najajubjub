class RecipeDisplay:
    
    def show_recipe(self, recipe):
        print("\n" + recipe["title"])
        
        used = []
        for ingredient in recipe["usedIngredients"]:
            used.append(ingredient["name"])
        
        missed = []
        for ingredient in recipe["missedIngredients"]:
            missed.append(ingredient["name"])
        
        if used:
            print("Used:", ", ".join(used))
        else:
            print("Used: None")
        
        if missed:
            print("Missing:", ", ".join(missed))
        else:
            print("Missing: Nothing!")
    
    def recipe_generator(self, recipes):
        for recipe in recipes:
            yield recipe

    def show_all_recipes(self, recipes):
        if not recipes:
            print("Enter a real ingredient bro")
            return
        
        for recipe in self.recipe_generator(recipes):
            self.show_recipe(recipe)