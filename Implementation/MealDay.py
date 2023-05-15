from click import launch


class MealDay:
    #self.day = day
    #tuple breakfast_opts = (bool skip, bool reheats_well, string price_range, string meat_type)
        #options for price_range: (cheap, medium, expensive, any)
        #options for meat_type: (vegan, vegetarian, beef, pork, chicken, turkey, seafood, any)
    #tuple lunch_opts = (bool skip, bool reheats_well, string price_range, string meat_type)
    #tuple dinner_opts = (bool skip, bool reheats_well, string price_range, string meat_type)

    def __init__(self, day):
        self.day = day
        self.breakfast_opts = {}
        self.lunch_opts = {}
        self.dinner_opts = {}

        self.breakfast_choice = None
        self.lunch_choice = None
        self.dinner_choice = None

        self.meals = [self.breakfast_choice, self.lunch_choice, self.dinner_choice]
    
    def add_options(self, meal, options = {}):
        if meal == "breakfast":
            self.breakfast_opts = options
        elif meal == "lunch":
            self.lunch_opts = options
        elif meal == "dinner":
            self.dinner_opts = options
        else:
            print("\n\nInvalid meal input type. Options are breakfast, lunch, dinner. You input" + str(meal))
        pass

    def get_choice(self, meal):
        if meal.lower() == "breakfast":
            return self.breakfast_choice
        elif meal.lower() == "lunch":
            return self.lunch_choice
        elif meal.lower() == "dinner":
            return self.dinner_choice
    
    def set_choice(self, meal, choice):
        if meal.lower() == "breakfast":
            self.breakfast_choice = choice
        elif meal.lower() == "lunch":
            self.lunch_choice = choice
        elif meal.lower() == "dinner":
            self.dinner_choice = choice
    


    




