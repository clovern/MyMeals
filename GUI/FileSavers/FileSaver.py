from tkinter import filedialog
import os
from datetime import date, timedelta
from Implementation.Meal import Meal

class FileSaver():

    #meal_plan should be a dictionary of MealDays, as created in MealPlanCreator
    def save_text_to_file(self, text):
        file = self.save_file()
        if file:

            file.write(text)
 
        if file:
            self.open_file(file)

    def save_file(self):
        file = filedialog.asksaveasfile(defaultextension ='.txt', filetypes = [("Text file", ".txt")])
        return file

    def open_file(self, file):
        os.startfile(file.name)