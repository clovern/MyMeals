from tkinter import *
from tkinter import ttk

class SpecialOptionsDropdown():
    def __init__(self, frame):

        self.frame = frame

        self.veganBool = IntVar()
        self.vegetarianBool = IntVar()
        self.chickenBool = IntVar()
        self.porkBool = IntVar()
        self.beefBool = IntVar()
        self.turkeyBool = IntVar()
        self.seafoodBool = IntVar()
        self.reheatsBool = IntVar()
        self.lowPriceBool = IntVar()
        self.mediumPriceBool = IntVar()
        self.highPriceBool = IntVar()

        self.dropdownVars = [self.veganBool, self.vegetarianBool, self.chickenBool, self.porkBool, self.beefBool, 
                             self.turkeyBool, self.seafoodBool, self.reheatsBool, self.lowPriceBool, self.mediumPriceBool, self.highPriceBool]

        self.dropdownOpts = [    'Vegan',
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
    
        self.createSpecialOptionsDropdown()

    def createSpecialOptionsDropdown(self):
        self.display= Menubutton (self.frame, text="            \u2193", relief=RAISED, background="white")
        self.display.menu = Menu ( self.display, tearoff = 0, background="white")
        self.display["menu"] = self.display.menu

        for index in range(len(self.dropdownOpts)):
            self.display.menu.add_checkbutton ( label=self.dropdownOpts[index],
            variable=self.dropdownVars[index] )     
    
    def getSelection(self): 
        selectedInitial = []
        selectedFinal = {}

        # adds all selected values directly into selectedInitial list
        for i in range(len(self.dropdownVars)):

            #value of 1 indicates this variable is selected
            if self.dropdownVars[i].get() == 1:
                selectedOption = self.dropdownOpts[i]
                selectedInitial.append(selectedOption)
        
        selectedFinal = self.formatSelection(selectedInitial)
                
        return selectedFinal
    
    def formatSelection(self, selectedInitial):
        
        selectedFinal = {}
        # If multiple values are selected for meat type or price, these selections are put into arrays.
        # This allows us to search for meals which match 1 or more of these options in MealCreator. 
        meat_types = []
        price_types = []
        for value in selectedInitial:
            if value.lower() in ["vegan", "vegetarian", "chicken", "pork", "beef", "turkey", "seafood"]:
                meat_types.append(value.lower())
            elif value in ["$", "$$", "$$$"]:
                if (value == "$"):
                    price_types.append("cheap")
                elif (value == "$$"):
                    price_types.append("medium")
                elif (value == "$$$"):
                    price_types.append("expensive")
            else:
                if (value.lower() == "reheats-well"):
                    selectedFinal["reheats_well"] = "true"

        if (len(meat_types) > 0):
            if (len(meat_types) == 1):
                selectedFinal["meat_type"] = meat_types[0]
            else:
                selectedFinal["meat_type"] = meat_types
        
        if (len(price_types) > 0):
            if (len(meat_types) == 1):
                selectedFinal["price_range"] = price_types[0]
            else:
                selectedFinal["price_range"] = price_types
                
        return selectedFinal