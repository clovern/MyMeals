import random
import json
from Meal import Meal
from MealDay import MealDay


class MealPlanCreator: 

    def __init__(self):
        self.all_meals = []
        self.breakfast_meals = []
        self.lunch_meals = []
        self.dinner_meals = []

        self.populate_default_meals()

        self.mealdays_dict = {"Monday": MealDay("Monday"), "Tuesday": MealDay("Tuesday"), "Wednesday": MealDay("Wednesday"), "Thursday": MealDay("Thursday"), "Friday": MealDay("Friday"), "Saturday": MealDay("Saturday"), "Sunday": MealDay("Sunday")}
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.day_to_index = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

        self.breakfast_meal_plan = []
        self.lunch_meal_plan = []
        self.dinner_meal_plan = []

        self.ingredients = {}       #a dictionary of ingredients, to build a grocery list

    def populate_default_meals(self): 
        default_file = open('default_meals.json')
        default_data = json.load(default_file)

        #create a meal object for each meal read
        for recipe in default_data:
            recipe_instructions = recipe['recipe'] if 'recipe' in recipe else None
            link = recipe['link'] if 'link' in recipe else None
            vegan_only = recipe['vegan_only'] if 'vegan_only' in recipe else "false"
            temp_meal = Meal(recipe['meal_name'], recipe['meat_type'], recipe['reheats_well'], recipe['price_range'], recipe['meal_type'], recipe_instructions, link, vegan_only, recipe['ingredients'])
            self.add_meal(temp_meal)
        default_file.close()

    def add_meal(self, meal):
        self.all_meals.append(meal)
        if meal.meal_type.lower() == "breakfast":
            self.breakfast_meals.append(meal)
        elif meal.meal_type.lower() == "lunch":
            self.lunch_meals.append(meal)
        elif meal.meal_type.lower() == "dinner":
            self.dinner_meals.append(meal)
    
    def set_meal_preference(self, day, meal, preferences):
        mealday = self.mealdays_dict[day]
        mealday.add_options(meal, preferences)

    
    def select_meal(self, mealday, meal):
        base_array = []
        
        if meal.lower() == "breakfast":
            base_array = self.breakfast_meals
            if "exclude" not in mealday.breakfast_opts:
                filtered_array = self.filter_meal_array(base_array, **mealday.breakfast_opts)
                mealday.breakfast_choice = self.random_meal(filtered_array) if len(filtered_array) > 0 else "N/A"
        
        elif meal.lower() == "lunch":
            base_array = self.lunch_meals
            if "exclude" not in mealday.lunch_opts.keys():
                filtered_array = self.filter_meal_array(base_array, **mealday.lunch_opts)
                mealday.lunch_choice = self.random_meal(filtered_array) if len(filtered_array) > 0 else "N/A"
        
        elif meal.lower() == "dinner":
            base_array = self.dinner_meals
            if "exclude" not in mealday.dinner_opts.keys():
                filtered_array = self.filter_meal_array(base_array, **mealday.dinner_opts)
                mealday.dinner_choice = self.random_meal(filtered_array) if len(filtered_array) > 0 else "N/A"

    def random_meal(self, filtered_array):
        if (len(filtered_array) > 0):
            return random.choice(filtered_array)
        return None
    
    def get_meal_selection(self, mealday, meal):
        return mealday.get_choice(meal)

    def set_chosen_meals(self, meal_selections):
        for day in meal_selections.keys():
            if meal_selections[day]["breakfast"] != None:
                self.mealdays_dict[day].set_choice("breakfast", meal_selections[day]["breakfast"])
            if meal_selections[day]["lunch"] != None:
                self.mealdays_dict[day].set_choice("lunch", meal_selections[day]["lunch"])
            if meal_selections[day]["dinner"] != None:
                self.mealdays_dict[day].set_choice("dinner", meal_selections[day]["dinner"])

    def get_mealdays_dict(self):
        return self.mealdays_dict
    
    def set_daily_preferences(self, weekly_preferences):
        breakfastindex = 0
        lunchindex = 1
        dinnerindex = 2

        for day in self.days:

            self.set_meal_preference(day, "breakfast", weekly_preferences[day][breakfastindex])
            self.set_meal_preference(day, "lunch", weekly_preferences[day][lunchindex])
            self.set_meal_preference(day, "dinner", weekly_preferences[day][dinnerindex])
            
        return

    def create_meal_plan(self, weekly_preferences):

        self.set_daily_preferences(weekly_preferences)

        # for mealday in self.mealdays_array:
        for mealday in self.mealdays_dict.values():
            self.select_meal(mealday, "breakfast")
            self.select_meal(mealday, "lunch")
            self.select_meal(mealday, "dinner")


    def filter_meal_array(self, base_array = None, **kwargs):
        if base_array == None:
            base_array = self.all_meals
        filtered_array = []
        
        #iterate through all meals, and add ones matching all kwargs to filtered_array
        for meal in base_array:
            match = True

            for key, value in kwargs.items():

                #this handles values like meat_type, where it can match one out of a list of options
                if type(value) == list:
                    
                    if (not getattr(meal, key) in value):
                        match = False
                        break
                
                #this handles values like meal_type, where it must match a singe passed value
                elif getattr(meal, key) != value:
                    match = False
                    break     

            #only add a meal if it matched all arguments.
            if match == True:
                filtered_array.append(meal)

        return filtered_array

        
