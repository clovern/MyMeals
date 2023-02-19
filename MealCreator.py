import random

class MealCreator: 

    def __init__(self):
        self.advanced = False
        self.use_fridge_pantry = False
        self.optimize_overlap = False
        self.advanced_options = []   #array of MealDay to store advanced options for each day

        self.all_meals = []   #array of Meal to store all the potential meal options

        self.breakfast_meal_plan = []
        self.lunch_meal_plan = []
        self.dinner_meal_plan = []
        self.ingredients = {}       #a dictionary of ingredients, to build a grocery list

    def set_advanced(self, advanced):
        self.advanced = advanced
    
    def set_optimize_overlap(optimize_overlap):
        optimize_overlap = optimize_overlap

    def add_meal(self, meal):
        self.all_meals.append(meal)
    
    def add_advanced_options(self, meal_day):
        self.advanced_options.append(meal_day)
    
    #creates a filtered array based on meal options
    #filtering occurs on base_array self.all_meals unless otherwise specified
    def create_filtered_array(self, base_array = None, **kwargs):
        if base_array == None:
            base_array = self.all_meals
        filtered_array = []
        
        #iterate through all meals, and add ones matching all kwargs to filtered_array
        for meal in base_array:
            match = True
            for key, value in kwargs.items():
                #if any value does not match, move on to next meal immediately
                #set match = False so that this meal will not be added
                if getattr(meal, key) != value:
                    match = False
                    break
            #only add a meal if it matched all arguments.
            if match == True:
                filtered_array.append(meal)

        return filtered_array


    def create_basic_plan(self, num_days = 7):
        self.dinner_meal_plan.clear()

        filtered_array = self.create_filtered_array(meal_type = 'dinner')
        
        #select num_meals random choices from all_meals
        for i in range(0, num_days):
            self.dinner_meal_plan.append(random.choice(filtered_array))
        
        return self.dinner_meal_plan

    def create_advanced_plan(self, mealdays_array):

        # filter out arrays for breakfast, lunch, and dinner meals
        breakfast_array = self.create_filtered_array(meal_type = 'breakfast')
        lunch_array = self.create_filtered_array(meal_type = 'lunch')
        dinner_array = self.create_filtered_array(meal_type = 'dinner')

        # add in all daily options for each meal, create an array of meals fitting those options
        # and select a random meal from the filtered array. 
        for mealday in mealdays_array:
            if mealday.breakfast_opts != None:
                filtered_array = self.create_filtered_array(breakfast_array, **mealday.breakfast_opts)
                mealday.breakfast_choice = random.choice(filtered_array)
            if mealday.lunch_opts != None:
                filtered_array = self.create_filtered_array(lunch_array, **mealday.lunch_opts)
                mealday.lunch_choice = random.choice(filtered_array)
            if mealday.dinner_opts != None:
                filtered_array = self.create_filtered_array(dinner_array, **mealday.dinner_opts)
                mealday.dinner_choice = random.choice(filtered_array)
        
