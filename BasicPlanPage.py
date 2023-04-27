from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage
from MealInfoDisplay import MealInfoDisplay
from DropdownTranslator import DropdownTranslator

class BasicPlanPage(PlanPage):
    def __init__(self, root, outer, previous):
        self.outer = outer
        self.previous = previous
        super().__init__()
        self.dropdown_list = []

        self.create_basic_plan_display()
    
    def create_basic_plan_display(self):
        self.create_upper_frame()
        self.create_lower_frame()
        self.center_in_frame()
        self.create_back_button()
        self.create_title("Basic Plan Creator")
        self.add_questions()
        self.create_submit_button()
    
    def add_questions(self):
        self.create_meal_question_prompt("breakfasts")
        self.create_meal_question_prompt("lunches")
        self.create_meal_question_prompt("dinners")
        self.special_options_prompt()
        self.set_dropdown_defaults()
    
    def create_meal_question_prompt(self, meal):
        self.question_frame= ttk.Frame(self.lowercontent)
        self.question_frame['padding'] = (15, 15, 15, 15)
        meal_question = 'How many {0} would you like planned this week?'.format(meal)
        self.meal_question_label = ttk.Label(self.question_frame, text=meal_question, font=("Arial", 15))
        self.create_number_dropdown()

        index = self.set_meal_index(meal)

        self.meal_question_label.grid(column=0, row=0, columnspan=3, sticky='E')
        (self.dropdown_list[-1]).grid(column=2, row=1, sticky='E', pady= (2,2))
        self.question_frame.grid(column=0, row=index)
    
    def create_submit_button(self):
        super().create_submit_button()
        self.submit_button.grid(column=0, columnspan=3, row=4)
    
    def create_number_dropdown(self):
        self.choice_selection = StringVar()
        self.basic_dropdown = ttk.Combobox(self.question_frame, textvariable=self.choice_selection)
        self.basic_dropdown['values'] = (
                            '0',
                            '1',
                            '2',
                            '3',
                            '4',
                            '5',
                            '6',
                            '7')
        self.dropdown_list.append(self.basic_dropdown)

    def center_in_frame(self):
        self.lowercontent.grid_columnconfigure(0, weight=1)
    
    def special_options_prompt(self):
        self.question_frame= ttk.Frame(self.lowercontent, width=600)
        self.question_frame['padding'] = (15, 15, 15, 15)

        self.meal_question_label = ttk.Label(self.question_frame, text="Special options?", font=("Arial", 15))
        self.create_special_options_dropdown(self.question_frame, "basic")

        self.meal_question_label.grid(column=0, row=0, columnspan = 3, sticky='E')
        self.special_dropdown.display.grid(column=2, row=1, pady = (2, 2))
        self.question_frame.grid(column=0, row=3)
    
    def set_dropdown_defaults(self):
        self.dropdown_list[0].current(7)
        self.dropdown_list[1].current(7)
        self.dropdown_list[2].current(7)

    def generate_plan(self):

        super().generate_plan()
        dropdown_translator = DropdownTranslator()
        weekly_preferences = dropdown_translator.set_weekly_preferences_basic(self.dropdown_list, self.special_dropdown)
        self.meal_creator.create_meal_plan(weekly_preferences)

        self.clear_page()
        display_meal_page = MealInfoDisplay(self.outer, self.meal_creator, self.content)
        
    def return_to_last_page(self):
        self.content.grid_forget()
        self.previous.grid(column=0, row=0)
