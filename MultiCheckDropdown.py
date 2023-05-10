from tkinter import *
from tkinter import ttk

class MultiCheckDropdown:
    def __init__(self, frame, options_list):
        self.frame = frame
        self.dropdown_opts = options_list
        self.create_dropdown()
    
    def create_dropdown_vars(self):
        self.dropdown_vars = []
        for i in range(len(self.dropdown_opts)):
            newVar = IntVar()
            self.dropdown_vars.append(newVar)
    
    def create_drodown(self):
        self.menu_button_text = "      \u2193"
        self.display= Menubutton (self.frame, text= self.menu_button_text, relief=RAISED, background="white", wraplength = 120)
        self.display.menu = Menu ( self.display, tearoff = 0, background="white")
        self.display["menu"] = self.display.menu

        for index in range(len(self.dropdown_opts)):
            label_text = self.dropdown_opts[index]
            self.display.menu.add_checkbutton (label=label_text,
            variable=self.dropdown_vars[index] , command = lambda index = index: self.handle_select(index))
        
    def handle_select(self, index):
        # FIXME
        print("IN HANDLESELECT")

    
