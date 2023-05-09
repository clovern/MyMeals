import json
from Meal import Meal

class MealDatabaseEditor:
    all_meals = []

    @staticmethod
    def populate_default_meals(): 
        default_file = open('default_meals.json')
        default_data = json.load(default_file)

        #create a meal object for each meal read
        for recipe in default_data:
            recipe_instructions = recipe['recipe'] if 'recipe' in recipe else None
            link = recipe['link'] if 'link' in recipe else None
            vegan_only = recipe['vegan_only'] if 'vegan_only' in recipe else "false"
            temp_meal = Meal(recipe['meal_name'], recipe['meat_type'], recipe['reheats_well'], recipe['price_range'], recipe['meal_type'], recipe_instructions, link, vegan_only, recipe['ingredients'])
            MealDatabaseEditor.add_meal(temp_meal)
        default_file.close()

    def add_meal(meal):
        MealDatabaseEditor.all_meals.append(meal)

    def get_all_meals():
        return MealDatabaseEditor.all_meals