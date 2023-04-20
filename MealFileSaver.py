from tkinter import filedialog
import os

class MealFileSaver():

    #meal_plan should be a dictionary of MealDays, as created in MealCreator
    @staticmethod
    def save_meal_plan(meal_plan):
        file = MealFileSaver.save_file()
        if file:
            for day in meal_plan:
                mealday = meal_plan[day]

                file.write("\n\n")
                file.write(mealday.day)
                file.write(": \n\n")

                file.write("\n")
                file.write("Breakfast:")
                file.write("\n")
                MealFileSaver.write_meal_to_file(file, mealday.breakfast_choice)
                
                file.write("\n")
                file.write("Lunch:")
                file.write("\n")
                MealFileSaver.write_meal_to_file(file, mealday.lunch_choice)
                
                file.write("\n")
                file.write("Dinner:")
                file.write("\n")
                MealFileSaver.write_meal_to_file(file, mealday.dinner_choice)
        
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
        file.write(ingredients)
        # instead, write the instructions for the meal and the recipe or link for the meal
        pass

    @staticmethod
    def open_file(file):
        os.startfile(file.name)
