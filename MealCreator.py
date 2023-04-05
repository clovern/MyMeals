import random
import json
from Meal import Meal
from MealDay import MealDay


class MealCreator: 

    def __init__(self):
        self.all_meals = []
        self.populate_default_meals()
        self.mealdays_dict = {"Monday": MealDay("Monday"), "Tuesday": MealDay("Tuesday"), "Wednesday": MealDay("Wednesday"), "Thursday": MealDay("Thursday"), "Friday": MealDay("Friday"), "Saturday": MealDay("Saturday"), "Sunday": MealDay("Sunday")}
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
            temp_meal = Meal(recipe['meal_name'], recipe['meat_type'], recipe['reheats_well'], recipe['price_range'], recipe['meal_type'], recipe['ingredients'])
            self.add_meal(temp_meal)
        default_file.close()

    def add_meal(self, meal):
        self.all_meals.append(meal)
    
    def set_mealday_preference(self, day, meal, preferences):
        # mealday = self.mealdays_array[self.day_to_index[day]]
        mealday = self.mealdays_dict[day]
        mealday.add_options(meal, preferences)
    
    def get_meal_choice(self, day, meal):
        day = self.mealdays_dict[day]
        if meal.lower() == "Breakfast":
            return day.breakfast_choice
        elif meal.lower() == "lunch":
            return day.lunch_choice
        elif meal.lower() == "dinner":
            return day.dinner_choice

    #creates a filtered array based on meal options
    def create_filtered_array(self, base_array = None, **kwargs):
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

    def create_meal_plan(self):

        # filter out arrays for breakfast, lunch, and dinner meals
        breakfast_array = self.create_filtered_array(meal_type = 'breakfast')
        lunch_array = self.create_filtered_array(meal_type = 'lunch')
        dinner_array = self.create_filtered_array(meal_type = 'dinner')

        # for mealday in self.mealdays_array:
        for mealday in self.mealdays_dict.values():

            #generate breakfast choices
            filtered_array = self.create_filtered_array(breakfast_array, **mealday.breakfast_opts)
            mealday.breakfast_choice = self.choose_meal(filtered_array)

            #generate lunch choices
            filtered_array = self.create_filtered_array(lunch_array, **mealday.lunch_opts)
            mealday.lunch_choice = self.choose_meal(filtered_array)

            #generate dinner choices
            filtered_array = self.create_filtered_array(dinner_array, **mealday.dinner_opts)
            mealday.dinner_choice = self.choose_meal(filtered_array)
    
    def choose_meal(self, filtered_array):
        if (len(filtered_array) > 0):
            return random.choice(filtered_array)
        return None
    
    def print_meals(self):
        for mealday in self.mealdays_dict.values():
            print(mealday.day + ":")
            if (mealday.breakfast_choice != None): 
                print("Breakfast: " + str(mealday.breakfast_choice))
            if (mealday.lunch_choice != None): 
                print("Lunch: " + str(mealday.lunch_choice))
            if (mealday.dinner_choice != None): 
                print("Dinner: " + str(mealday.dinner_choice))
            print()

        
