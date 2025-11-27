from config import Setting
from janitor import clean_ingredient, correct_input
from finder import RecipeFinder


def main():
    print("Recipe finder started")
    
    try:
        setting = Setting()
        finder = RecipeFinder(setting)
        
        ingredient_input = input("Enter your ingredients seperate each one by comma (,) ok? ").lower()

        if not correct_input(ingredient_input):
            return

        ingredient = clean_ingredient(ingredient_input)
        if not ingredient:
            print("What did you even type. Try again!")
            return

        recipes = finder.search(ingredient)
        if not recipes:
            print("No recipe found cant find any bro")
            return

        finder.display.show_all_recipes(recipes)

    except Exception as e:
        print("Something went wrong bro", e)
    finally:
        print("Thank you for using")


if __name__ == "__main__":
    main()