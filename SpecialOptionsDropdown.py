from tkinter import *
from tkinter import ttk

class SpecialOptionsDropdown():
    def __init__(self, frame, type, base_page = None):

        self.frame = frame
        self.type = type
        self.base_page = base_page

        self.vegan_bool = IntVar()
        self.vegetarian_bool = IntVar()
        self.chicken_bool = IntVar()
        self.pork_bool = IntVar()
        self.beef_bool = IntVar()
        self.turkey_bool = IntVar()
        self.seafood_bool = IntVar()
        self.reheats_bool = IntVar()
        self.low_price_bool = IntVar()
        self.medium_price_bool = IntVar()
        self.high_price_bool = IntVar()

        self.dropdown_vars = [self.vegan_bool, self.vegetarian_bool, self.chicken_bool, self.pork_bool, self.beef_bool, 
                             self.turkey_bool, self.seafood_bool, self.reheats_bool, self.low_price_bool, self.medium_price_bool, self.high_price_bool]

        self.dropdown_opts = [    'Vegan',
                    'Vegetarian',
                    'Chicken',
                    'Pork',
                    'Beef',
                    'Turkey',
                    'Seafood',
                    'Reheats-well',
                    '$',
                    '$$',
                    '$$$']
        
        self.create_special_options_dropdown(type)

    def create_special_options_dropdown(self, type):
        self.menu_button_text = self.get_dropdown_default_text()
        self.display= Menubutton (self.frame, text= self.menu_button_text, relief=RAISED, background="white", wraplength = 120)
        self.display.menu = Menu ( self.display, tearoff = 0, background="white")
        self.display["menu"] = self.display.menu

        if self.type == "advanced":
            self.make_advanced()
        
        if self.type == "filter":
            self.make_filter()

        for index in range(len(self.dropdown_opts)):
            label_text = self.dropdown_opts[index]
            self.display.menu.add_checkbutton (label=label_text,
            variable=self.dropdown_vars[index] , command = lambda index = index: self.display_option(index))
    
    def display_option(self, index):

        label_text = ""

        len_labels = 0

        if self.dropdown_opts[index] == "Exclude this Meal":
            if (self.exclude_bool.get() != 0):
                label_text = "Exclude this Meal \u2193"
                for var in self.dropdown_vars:
                    var.set(0)
                len_labels += 1
                self.exclude_bool.set(1)

        else:
            for i in range(len(self.dropdown_vars)):
                if self.type == "advanced":
                    self.exclude_bool.set(0)
                if self.dropdown_vars[i].get() == 1:
                    len_labels += 1
                    if len_labels > 0:
                        label_text = ", " + label_text
                    label_text = self.dropdown_opts[i] + label_text
                    if self.type == "filter":
                        if len_labels >= 2:
                            label_text = label_text + " ..."
                            break
            label_text += " \u2193"
        
        if len_labels == 0:
            label_text = self.get_dropdown_default_text()
        
        self.display.configure(text = label_text)

        if self.type == "filter":
            self.update_base_page()
    
    def update_base_page(self):

        self.base_page.update_results_for_filter(self.get_selection())
    
    def get_dropdown_default_text(self):
        default_label = " \u2193"
        if self.type == "filter":
            default_label = " \u23DA    Filter    " + default_label
        else: 
            default_label = "          " + default_label
        return default_label

    def make_advanced(self):
        self.dropdown_opts.insert(0, "Exclude this Meal")
        self.exclude_bool = IntVar()
        self.dropdown_vars.insert(0, self.exclude_bool)
    
    def make_filter(self):

        self.dropdown_opts.insert(0, "Dinner")
        self.dinner_bool = IntVar()
        self.dropdown_vars.insert(0, self.dinner_bool)

        self.dropdown_opts.insert(0, "Lunch")
        self.lunch_bool = IntVar()
        self.dropdown_vars.insert(0, self.lunch_bool)

        self.dropdown_opts.insert(0, "Breakfast")
        self.breakfast_bool = IntVar()
        self.dropdown_vars.insert(0, self.breakfast_bool)


    def set_exclude(self):
        self.exclude_bool.set(1)
        self.display.configure(text = "Exclude this Meal \u2193")

    def get_selection(self): 
        selected_initial = []
        selected_final = {}

        # adds all selected values directly into selected_initial list
        for i in range(len(self.dropdown_vars)):

            #value of 1 indicates this variable is selected
            if self.dropdown_vars[i].get() == 1:
                selected_option = self.dropdown_opts[i]
                selected_initial.append(selected_option)
        
        selected_final = self.format_selection(selected_initial)
                
        return selected_final
    
    def format_selection(self, selected_initial):
        
        selected_final = {}
        # If multiple values are selected for meat type or price, these selections are put into arrays.
        # This allows us to search for meals which match 1 or more of these options in MealPlanCreator. 
        meat_types = []
        price_types = []
        meal_types = []

        for value in selected_initial:
            if value.lower() == "exclude this meal":
                selected_final["exclude"] = "true"
                return selected_final
            
            if value.lower() in ["vegan", "vegetarian", "chicken", "pork", "beef", "turkey", "seafood"]:
                #vegan meals not specified as vegan_only should be included when someone selects vegetarian.
                if value.lower() == "vegetarian":
                    selected_final["vegan_only"] = "false"
                    if "vegan" not in meat_types:
                        meat_types.append("vegan")

                if value.lower() == "vegan":
                    if "Vegetarian" not in selected_initial:
                        selected_final["vegan_only"] = ["true", "false"]

                if value.lower() != "vegan":
                    meat_types.append(value.lower())
                elif "vegan" not in meat_types:
                    meat_types.append("vegan")

            elif value in ["$", "$$", "$$$"]:
                if (value == "$"):
                    price_types.append("cheap")
                elif (value == "$$"):
                    price_types.append("medium")
                elif (value == "$$$"):
                    price_types.append("expensive")

            elif value.lower() in ["breakfast", "lunch", "dinner"]:
                meal_types.append(value.lower())

            else:
                if (value.lower() == "reheats-well"):
                    selected_final["reheats_well"] = "true"

        if (len(meat_types) > 0):
            if (len(meat_types) == 1):
                selected_final["meat_type"] = meat_types[0]
            else:
                selected_final["meat_type"] = meat_types
        
        if (len(price_types) > 0):
            if (len(meat_types) == 1):
                selected_final["price_range"] = price_types[0]
            else:
                selected_final["price_range"] = price_types
        
        if (len(meal_types) > 0):
            if (len(meal_types) == 1):
                selected_final["meal_type"] = meal_types[0]
            else:
                selected_final["meal_type"] = meal_types
        
        return selected_final