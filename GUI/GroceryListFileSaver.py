from tkinter import filedialog
import os
from datetime import date, timedelta
from Implementation.Meal import Meal
from GUI.FileSaver import FileSaver

class GroceryListFileSaver(FileSaver):

    def __init__(self):
        self.meal_text = "" 
        self.ingredients_dict = {}
        self.grocery_list_string = ""

    #meal_plan should be a dictionary of MealDays, as created in MealPlanCreator
    def generate_file_text(self, meal_plan):

        start_date = date.today()
        end_date = start_date + timedelta(days=7)

        self.meal_text +="Grocery List for " + str(start_date) + " - " + str(end_date) + ":\n\n"
        for day in meal_plan:
            mealday = meal_plan[day]

            if isinstance(mealday.breakfast_choice, Meal):
                self.write_ingredients_to_dict(mealday.breakfast_choice)
            
            if isinstance(mealday.lunch_choice, Meal):
                self.write_ingredients_to_dict(mealday.lunch_choice)
            
            if isinstance(mealday.dinner_choice, Meal):
                self.write_ingredients_to_dict(mealday.dinner_choice)
        
        self.write_dict_to_string()
        
        return self.meal_text + self.grocery_list_string
    
    def write_ingredients_to_dict(self, meal):
        if len(meal.ingredients) == 0:
            self.ingredients_dict[meal.name] = "No ingredients list"
        
        for ingredient in meal.ingredients.keys():

            if ingredient in self.ingredients_dict:
                ingred_array = meal.ingredients[ingredient]
                # checks if the unit of measurement already exists for the measurement. If so, adds the amount together. 
                try:
                    match_index = self.ingredients_dict[ingredient].index(ingred_array[1])
                    previous_amount = float(self.ingredients_dict[ingredient][match_index - 1])
                    new_amount = previous_amount + float(ingred_array[0])
                    self.ingredients_dict[ingredient][match_index - 1] = str(new_amount)
                except:
                    self.ingredients_dict[ingredient].append(ingred_array[0])
                    self.ingredients_dict[ingredient].append(ingred_array[1])
            else:
                self.ingredients_dict[ingredient] = meal.ingredients[ingredient]
        
    def write_dict_to_string(self):

        for ingredient in self.ingredients_dict:
            ingredient_string = ""
            # This indicates that there were no ingredients listed for a meal, which should be indicated on grocery list
            if self.ingredients_dict[ingredient] == "No ingredients list":
                mealname = ingredient
                ingredient_string += "No ingredients listed for " + mealname + ". Add manually as needed."
            else:
                ingredient_string = ingredient + ", " 
                ingredient_amounts_list = self.ingredients_dict[ingredient]

                counter = 0
                # adds each ingredient to grocery list. Adds a + between ingredient measurements of different units. 
                for val in ingredient_amounts_list:
                    if counter > 2 & (counter % 2 != 0):
                        ingredient_string += "+"
                    ingredient_string += " " + val

            self.grocery_list_string += ingredient_string + "\n"
