

# turns a dict of dropdown menus from the GUI into a dictionary of weekly preferences that can 
# be passed into MealCreator
class DropdownTranslator():
    def __init__(self):
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.weekly_preferences = {"Monday": [{}, {}, {}], "Tuesday": [{}, {}, {}], "Wednesday": [{}, {}, {}], "Thursday": [{}, {}, {}],
                            "Friday": [{}, {}, {}], "Saturday": [{}, {}, {}], "Sunday": [{}, {}, {}]}


    def set_weekly_preferences_advanced(self, dropdown_dict):

        #add selected options from each day to weekly_preferences, as an array
        for day in self.days:
            index = 0
            for meal in ["breakfast", "lunch", "dinner"]:
                dropdown = dropdown_dict[day][meal]
                self.weekly_preferences[day][index] = (dropdown.get_selection())
                index += 1

        return self.weekly_preferences
    
    def set_weekly_preferences_basic(self, dropdown_list, special_dropdown):

        preferences = special_dropdown.get_selection()
        breakfast_num = int(dropdown_list[0].get())
        lunch_num = int(dropdown_list[1].get())
        dinner_num = int(dropdown_list[2].get())

        self.set_basic_preferences_helper(breakfast_num, "breakfast", preferences)
        self.set_basic_preferences_helper(lunch_num, "lunch", preferences)
        self.set_basic_preferences_helper(dinner_num, "dinner", preferences)

        return self.weekly_preferences
    
    def set_basic_preferences_helper(self, num_meals, meal_name, preferences):

        meal_index = 0
        if meal_name == "lunch":
            meal_index = 1
        if meal_name == "dinner":
            meal_index = 2

        #set the selected preference(s) on the wanted number of meals
        for i in range(num_meals):
            self.weekly_preferences[self.days[i]][meal_index] = preferences
            
        #indicate that the remaining meals should be excluded
        for i in range(num_meals, 7):
            self.weekly_preferences[self.days[i]][meal_index] = {"exclude": "true"}