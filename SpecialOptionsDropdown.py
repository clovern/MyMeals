from tkinter import *
from tkinter import ttk

class SpecialOptionsDropdown():
    def __init__(self, frame):

        self.frame = frame

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
        
        self.create_special_options_dropdown()

    def create_special_options_dropdown(self):
        self.menu_button_text = "           \u2193"
        self.display= Menubutton (self.frame, text= self.menu_button_text, relief=RAISED, background="white")
        self.display.menu = Menu ( self.display, tearoff = 0, background="white")
        self.display["menu"] = self.display.menu

        for index in range(len(self.dropdown_opts)):
            self.display.menu.add_checkbutton (label=self.dropdown_opts[index],
            variable=self.dropdown_vars[index] , command = lambda: self.display_option(self.display))
    
    def display_option(self, menu_button):
        # FIXME
        self.menu_button_text = "testText\u2193"
        menu_button.configure(text = self.menu_button_text)

    def make_advanced(self):
        self.dropdown_opts.insert(0, "Exclude this Meal")
        self.exclude_bool = IntVar()
        self.dropdown_vars.insert(0, self.exclude_bool)
        self.display.menu.add_checkbutton ( label=self.dropdown_opts[0],
            variable=self.dropdown_vars[0] )

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
        # This allows us to search for meals which match 1 or more of these options in MealCreator. 
        meat_types = []
        price_types = []
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
                        selected_final["vegan_only"] = "true"

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
        
        return selected_final