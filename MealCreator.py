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
        mealday = self.mealdays_dict[day]
        mealday.add_options(meal, preferences)
    
    def select_meal(self, filtered_array):
        if (len(filtered_array) > 0):
            return random.choice(filtered_array)
        return None
    
    def get_meal_selection(self, day, meal):
        day = self.mealdays_dict[day]
        if meal.lower() == "breakfast":
            return day.breakfast_choice
        elif meal.lower() == "lunch":
            return day.lunch_choice
        elif meal.lower() == "dinner":
            return day.dinner_choice
    
    def setWeeklyPreferencesAdvanced(self, dropdownDict):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.weeklyPreferences = {"Monday": [{}, {}, {}], "Tuesday": [{}, {}, {}], "Wednesday": [{}, {}, {}], "Thursday": [{}, {}, {}],
                        "Friday": [{}, {}, {}], "Saturday": [{}, {}, {}], "Sunday": [{}, {}, {}]}

        #add selected options from each day to weeklyPreferences, as an array
        for day in self.days:
            for index in range(3):
                dropdown = dropdownDict[day][index]
                self.weeklyPreferences[day][index] = (dropdown.getSelection())

        self.setDailyPreferences(self.weeklyPreferences)
    
    def setWeeklyPreferencesBasic(self, dropdownList, specialDropdown):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.weeklyPreferences = {"Monday": [{}, {}, {}], "Tuesday": [{}, {}, {}], "Wednesday": [{}, {}, {}], "Thursday": [{}, {}, {}],
                        "Friday": [{}, {}, {}], "Saturday": [{}, {}, {}], "Sunday": [{}, {}, {}]}

        preferences = specialDropdown.getSelection()

        breakfastNum = int(dropdownList[0].get())
        lunchNum = int(dropdownList[1].get())
        dinnerNum = int(dropdownList[2].get())

        self.set_basic_preferences_helper(breakfastNum, "breakfast", preferences)
        self.set_basic_preferences_helper(lunchNum, "lunch", preferences)
        self.set_basic_preferences_helper(dinnerNum, "dinner", preferences)

        self.setDailyPreferences(self.weeklyPreferences)
    
    def set_basic_preferences_helper(self, num_meals, meal_name, preferences):

        meal_index = 0
        if meal_name == "lunch":
            meal_index = 1
        if meal_name == "dinner":
            meal_index = 2

        #set the selected preference(s) on the wanted number of meals
        for i in range(num_meals):
            meal_value = self.weeklyPreferences[self.days[i]][meal_index]
            self.weeklyPreferences[self.days[i]][meal_index] = preferences
            
        #indicate that the remaining meals should be excluded
        for i in range(num_meals, 7):
            self.weeklyPreferences[self.days[i]][meal_index] = {"exclude": "true"}
    
    def setDailyPreferences(self, weeklyPreferences):
        breakfastindex = 0
        lunchindex = 1
        dinnerindex = 2

        for day in self.days:

            self.set_mealday_preference(day, "breakfast", weeklyPreferences[day][breakfastindex])
            self.set_mealday_preference(day, "lunch", weeklyPreferences[day][lunchindex])
            self.set_mealday_preference(day, "dinner", weeklyPreferences[day][dinnerindex])
            
        return

    def create_meal_plan(self):

        # filter out arrays for breakfast, lunch, and dinner meals
        breakfast_array = self.filter_meal_array(meal_type = 'breakfast')
        lunch_array = self.filter_meal_array(meal_type = 'lunch')
        dinner_array = self.filter_meal_array(meal_type = 'dinner')

        # for mealday in self.mealdays_array:
        for mealday in self.mealdays_dict.values():

            #generate breakfast choices
            if "exclude" not in mealday.breakfast_opts:
                filtered_array = self.filter_meal_array(breakfast_array, **mealday.breakfast_opts)
                mealday.breakfast_choice = self.select_meal(filtered_array)

            #generate lunch choices
            if "exclude" not in mealday.lunch_opts.keys():
                filtered_array = self.filter_meal_array(lunch_array, **mealday.lunch_opts)
                mealday.lunch_choice = self.select_meal(filtered_array)

            #generate dinner choices
            if "exclude" not in mealday.dinner_opts.keys():
                filtered_array = self.filter_meal_array(dinner_array, **mealday.dinner_opts)
                mealday.dinner_choice = self.select_meal(filtered_array)
    
        #creates a filtered array based on meal options
    
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

        
