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