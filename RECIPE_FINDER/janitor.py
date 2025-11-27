def clean_ingredient(ingredient_input):
   
    ingredient_list = ingredient_input.split(",")
    
    cleaned_list = []
    
    for item in ingredient_list:
        item = item.strip()  
        if item != "":
            cleaned_list.append(item)
    
    return ",".join(cleaned_list)

def correct_input(ingredient_input):
    if not ingredient_input.strip():
        print("You didn't enter anything bro")
        return False
    return True