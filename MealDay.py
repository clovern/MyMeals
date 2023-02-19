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
        self.breakfast_opts = None
        self.lunch_opts = None
        self.dinner_opts = None

        self.breakfast_choice = None
        self.lunch_choice = None
        self.dinner_choice = None
    
    def add_options(self, meal, options = {}):
        if meal == "breakfast":
            self.breakfast_opts = options
        elif meal == "lunch":
            self.lunch_opts = options
        elif meal == "dinner":
            self.dinner_opts = options
        else:
            print("\n\nInvalid meal input type. Options are breakfast, lunch, dinner. You input" + str(meal))
    


    




