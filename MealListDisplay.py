from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PlanPage import PlanPage
from idlelib.tooltip import Hovertip
from SpecialOptionsDropdown import SpecialOptionsDropdown
from Meal import Meal
from MealPlanCreator import MealPlanCreator
from PIL import Image
from PIL import ImageTk

class MealListDisplay(PlanPage):

    def __init__(self, outer, previous):
        self.outer = outer
        self.previous = previous
        super().__init__()
        self.all_meals = []
        self.upload_meals()
        self.display_start = 0
        self.create_meal_display()
    
    def create_meal_display(self):
        self.lowercontent["height"] = 600
        self.create_title("Meal List")
        self.create_back_button()
        self.display_upper_buttons()
        self.display_lower_buttons()
        self.display_meals_body()

    def upload_meals(self):
        # FIXME should fix how this is done later
        self.meal_plan_creator = MealPlanCreator()
        self.all_meals = self.meal_plan_creator.all_meals
    
    def display_upper_buttons(self):
        self.upperbuttons_frame = ttk.Frame(self.lowercontent, height = 75, width=800)
        self.upperbuttons_frame.pack_propagate(0)
        self.upperbuttons_frame.grid(column = 0, row =0)
        self.create_upper_buttons()
    
    def create_upper_buttons(self):
        self.create_addmeals_button()
        self.create_filter_dropdown()

    def create_addmeals_button(self):
        # FIXME
        mealday = None
        meal = None

        self.addmeals_button = ttk.Button(self.upperbuttons_frame, text="\u2795 Add Meals", width = 15, default="active", command=lambda: self.show_meal_details(mealday, meal))
        self.addmeals_button.pack(anchor = E, padx = (20, 20), pady = (0, 10))
    
    def show_meal_details(self, mealday, meal):
        pass

    def create_filter_dropdown(self):
        self.filter = SpecialOptionsDropdown(self.upperbuttons_frame, "filter", self)
        self.filter.display["width"] = 15
        self.filter.display["wraplength"] = 100
        self.filter.display.pack(anchor = E, padx = (20, 20), pady = (0, 10))

    def display_meals_body(self):
        self.displaymeals_frame = ttk.Frame(self.lowercontent, height = 600, width=800)
        self.displaymeals_frame.grid(column = 0, row =1)
        self.populate_meals()
    
    def populate_meals(self):
        if len(self.all_meals) == 0:
            self.display_meal(None)
        end_index = min(len(self.all_meals), self.display_start + 11)
        for meal in self.all_meals[self.display_start : end_index]:
            self.display_meal(meal)
    
    def display_meal(self, meal):
        self.meal_frame = ttk.Frame(self.displaymeals_frame, borderwidth=1, relief="solid")
        if meal != None:
            self.create_remove_button(meal)
            self.create_meal_label(meal)
            self.create_details_button(meal)
        else:
            self.create_meal_label(None)
        self.meal_frame.pack(pady = (5, 5))
    
    def create_remove_button(self, meal):
        self.remove_button = ttk.Button(self.meal_frame, text="\u2796", width = 3, default="active", command=lambda: self.remove_meal(meal))
        self.remove_button.grid(column = 0, row = 0)
        Hovertip(self.remove_button, "Remove this meal")
    
    def remove_meal(self, meal):
        pass

    def create_meal_label(self, meal):
        label_text = "No meals match the criteria"
        if meal != None:
            label_text = meal.name
        meal_label = Label(self.meal_frame, text=label_text, justify = CENTER, width = 90, wraplength = 600)
        meal_label.grid(column = 1, row = 0)
        pass

    def create_details_button(self, meal):
        self.details_button = ttk.Button(self.meal_frame, text=u"\U0001F441", width = 3, default="active", command=lambda: self.show_meal_details(meal))
        self.details_button.grid(column = 2, row = 0)
        Hovertip(self.details_button, "Details")
    
    def show_meal_details(self, meal):
        pass

    def display_lower_buttons(self):
        self.lowerbuttons_frame = ttk.Frame(self.lowercontent, width = 800, height = 50)
        self.lowerbuttons_frame.pack_propagate(0)
        self.lowerbuttons_frame.grid(column = 0, row = 2, pady = (20, 0))
        self.create_lower_buttons()
    
    def create_lower_buttons(self):
        self.scrollbuttons_frame = ttk.Frame(self.lowerbuttons_frame)
        self.create_scroll_down_button()
        self.create_scroll_up_button()
        self.scrollbuttons_frame.pack(anchor = E, padx = (0, 20), pady= (5, 0))
    
    def create_scroll_down_button(self):
        self.downarrow_image = Image.open("./down_arrow.jpg")
        self.downarrow_image = (self.downarrow_image).resize((30,30))
        self.downarrow_image = ImageTk.PhotoImage(self.downarrow_image)
        self.show_next_button = ttk.Button(self.scrollbuttons_frame, image=self.downarrow_image, text="\u2795 Add Meals", width = 15, default="active", command=lambda: self.show_next_meals())
        self.show_next_button.grid(column=1, row=0)
        Hovertip(self.show_next_button, "View next meals")
    
    def show_next_meals(self):
        self.display_start = self.display_start + 11
        if self.display_start >= len(self.all_meals):
            self.display_start = self.display_start - 11
            messagebox.showinfo("", "You have reached the end of the Recipe Book.")
        else: 
            self.displaymeals_frame.destroy()
            self.display_meals_body()

    def create_scroll_up_button(self):
        self.uparrow_image = Image.open("./up_arrow.jpg")
        self.uparrow_image = (self.uparrow_image).resize((30,30))
        self.uparrow_image = ImageTk.PhotoImage(self.uparrow_image)
        self.show_previous_button = ttk.Button(self.scrollbuttons_frame, image=self.uparrow_image, text="\u2795 Add Meals", width = 15, default="active", command=lambda: self.show_previous_meals())
        self.show_previous_button.grid(column=0, row=0)
        Hovertip(self.show_previous_button, "View previous meals")
    
    def show_previous_meals(self):
        self.display_start = self.display_start - 11
        if self.display_start < 0:
            self.display_start = self.display_start + 11
            messagebox.showinfo("", "You have reached the beginning of the Recipe Book.")
        else: 
            self.displaymeals_frame.destroy()
            self.display_meals_body()
    
    def update_results_for_filter(self, selection):
        self.all_meals = self.meal_plan_creator.filter_meal_array(self.meal_plan_creator.all_meals, **selection)
        self.displaymeals_frame.destroy()
        self.display_meals_body()