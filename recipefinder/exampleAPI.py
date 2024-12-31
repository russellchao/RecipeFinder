#################################### 
# EXAMPLE USAGE OF SPOONACULAR API #
####################################

import requests

API_KEY = 'ef8163f9b5d64b61a449552724d38c15'

def get_recipes(ingredients):
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

# Example usage
ingredients = "apples,flour,sugar"
recipes = get_recipes(ingredients)
for recipe in recipes:
    print(f"Recipe: {recipe['title']}, ID: {recipe['id']}")


#### Output of following code ####

# Recipe: Cranberry Apple Crisp, ID: 640352
# Recipe: Apricot Glazed Apple Tart, ID: 632660
# Recipe: Easy & Delish! ~ Apple Crumble, ID: 641803
# Recipe: Apple Or Peach Strudel, ID: 73420
# Recipe: Apple Cinnamon Blondies, ID: 157103