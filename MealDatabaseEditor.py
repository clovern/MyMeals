import json
from Meal import Meal

class MealDatabaseEditor:
    all_meals = []
    updated = True
    default_data = None

    @staticmethod
    def populate_default_meals(): 
        MealDatabaseEditor.all_meals = []
        default_file = open('default_meals.json')
        MealDatabaseEditor.default_data = json.load(default_file)

        #create a meal object for each meal read
        for recipe in MealDatabaseEditor.default_data:
            recipe_instructions = recipe['recipe'] if 'recipe' in recipe else None
            link = recipe['link'] if 'link' in recipe else None
            vegan_only = recipe['vegan_only'] if 'vegan_only' in recipe else "false"
            temp_meal = Meal(recipe['meal_name'], recipe['meat_type'], recipe['reheats_well'], recipe['price_range'], recipe['meal_type'], recipe_instructions, link, vegan_only, recipe['ingredients'])
            MealDatabaseEditor.upload_meal_to_array(temp_meal)
        default_file.close()

    def upload_meal_to_array(meal):
        MealDatabaseEditor.all_meals.append(meal)
    
    def remove_meal(mealname):
        # get the index of the meal that I want to remove. 
        numMeals = len(MealDatabaseEditor.default_data)
        for i in range(numMeals):
            if MealDatabaseEditor.default_data[i]["meal_name"] == mealname:
            # remove that index from the array using array.pop probably?
                MealDatabaseEditor.default_data.pop(i)
                break
        # make this back into a json
        with open('default_meals.json', "w") as f:
            json.dump(MealDatabaseEditor.default_data, f, indent = 6)
        

        # update the all_meals array for change
        MealDatabaseEditor.all_meals.clear()
        MealDatabaseEditor.populate_default_meals()
        MealDatabaseEditor.updated = True
    
    def add_meal(meal):
        newmeal_object = MealDatabaseEditor.json_format_meal(meal)
        MealDatabaseEditor.default_data.append(newmeal_object)
        with open('default_meals.json', "w") as f:
            json.dump(MealDatabaseEditor.default_data, f, indent = 6)
        
        # update the all_meals array for change
        MealDatabaseEditor.all_meals.clear()
        MealDatabaseEditor.populate_default_meals()
        MealDatabaseEditor.updated = True

    def json_format_meal(meal):
        newmeal_object = {}
        newmeal_object["meal_name"] = meal.name
        newmeal_object["meat_type"] = meal.meat_type
        newmeal_object["reheats_well"] = meal.reheats_well
        newmeal_object["price_range"] = meal.price_range
        newmeal_object["meal_type"] = meal.meal_type
        newmeal_object["ingredients"] = meal.ingredients
        if meal.recipe != None:
            newmeal_object["recipe"] = meal.recipe
        if meal.link != None:
            newmeal_object["link"] = meal.link
        newmeal_object["vegan_only"] = meal.vegan_only

        return newmeal_object


    def get_all_meals():
        return MealDatabaseEditor.all_meals