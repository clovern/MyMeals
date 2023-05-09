import json
from Meal import Meal

class MealDatabaseEditor:
    all_meals = []
    default_data = None

    @staticmethod
    def populate_default_meals(): 
        default_file = open('default_meals.json')
        MealDatabaseEditor.default_data = json.load(default_file)
        # FIXME
        print("DEFAULT DATA")
        print(MealDatabaseEditor.default_data)

        #create a meal object for each meal read
        for recipe in MealDatabaseEditor.default_data:
            recipe_instructions = recipe['recipe'] if 'recipe' in recipe else None
            link = recipe['link'] if 'link' in recipe else None
            vegan_only = recipe['vegan_only'] if 'vegan_only' in recipe else "false"
            temp_meal = Meal(recipe['meal_name'], recipe['meat_type'], recipe['reheats_well'], recipe['price_range'], recipe['meal_type'], recipe_instructions, link, vegan_only, recipe['ingredients'])
            MealDatabaseEditor.add_meal(temp_meal)
        default_file.close()

    def add_meal(meal):
        MealDatabaseEditor.all_meals.append(meal)
    
    def remove_meal(mealname):
        # get the index of the meal that I want to remove. 
        numMeals = len(MealDatabaseEditor.default_data)
        for i in range(numMeals):
            if MealDatabaseEditor.default_data[i]["meal_name"] == mealname:
            # remove that index from the array using array.pop probably?
                popped = MealDatabaseEditor.default_data.pop(i)
                # FIXME
                print("POPPED")
                print(popped)
                break
        # make this back into a json
        with open('default_meals.json', "w") as f:
            json.dump(MealDatabaseEditor.default_data, f, indent = 6)

    def get_all_meals():
        return MealDatabaseEditor.all_meals