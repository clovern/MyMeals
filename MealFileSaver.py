from tkinter import filedialog
import os
from datetime import date, timedelta
from Meal import Meal

class MealFileSaver():


    #meal_plan should be a dictionary of MealDays, as created in MealCreator
    @staticmethod
    def save_meal_plan(meal_plan):
        file = MealFileSaver.save_file()
        if file:

            start_date = date.today()
            end_date = start_date + timedelta(days=7)

            file.write("Meal plan for " + str(start_date) + " - " + str(end_date))
            for day in meal_plan:
                mealday = meal_plan[day]

                file.write("\n\n")
                file.write("_____________________________________________________________________________________\n")
                file.write(mealday.day)
                file.write(": \n\n")

                if isinstance(mealday.breakfast_choice, Meal):
                    file.write("\n")
                    file.write("Breakfast:\n")
                    file.write("\n")
                    MealFileSaver.write_meal_to_file(file, mealday.breakfast_choice)
                
                if isinstance(mealday.lunch_choice, Meal):
                    file.write("\n")
                    file.write(".   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .\n")
                    file.write("Lunch:\n")
                    file.write("\n")
                    MealFileSaver.write_meal_to_file(file, mealday.lunch_choice)
                
                if isinstance(mealday.dinner_choice, Meal):
                    file.write("\n")
                    file.write(".   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .\n")
                    file.write("Dinner:\n")
                    file.write("\n")
                    MealFileSaver.write_meal_to_file(file, mealday.dinner_choice)
            
        if file:
            MealFileSaver.open_file(file)

    @staticmethod
    def save_file():
        file = filedialog.asksaveasfile(defaultextension ='.txt', filetypes = [("Text file", ".txt")])
        return file

    @staticmethod
    def write_meal_to_file(file, meal):
        file.write(meal.name)
        file.write("\n")
        ingredients = meal.format_meal_ingredients()
        file.write("\n" + ingredients)
        recipe_or_link = meal.format_link_or_recipe_text()
        file.write("\n" + recipe_or_link)

    @staticmethod
    def open_file(file):
        os.startfile(file.name)
