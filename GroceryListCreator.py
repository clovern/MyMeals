import random
import json
from Meal import Meal
from MealDay import MealDay
from MealPlanCreator import MealPlanCreator

class GroceryListCreator: 

    def __init__(self):
        self.grocery_list_text = "\nGrocery List: \n\n"

    def create_grocery_list(self, mealdays_dict):
        for day in mealdays_dict.keys():
            self.write_ingredients(mealdays_dict[day].get_choice("breakfast"))
            self.write_ingredients(mealdays_dict[day].get_choice("lunch"))
            self.write_ingredients(mealdays_dict[day].get_choice("dinner"))
        
    def write_ingredients(self, meal):
        # FIXME 
        print("IN WRITE INGREDIENTS")
        print(meal.ingredients)