from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
from PIL import Image
from PIL import ImageTk
from idlelib.tooltip import Hovertip
from Implementation.MealSearcher import MealSearcher

class MealSearcherPopup:

    def __init__(self, base_page, advanced_opts = None):
        self.base_page = base_page
        if advanced_opts != None:
            self.meal = advanced_opts["meal"]
            self.day = advanced_opts["day"]
            self.frame = advanced_opts["frame"]
            self.advanced_page = True
        else:
            self.advanced_page = False
        self.build_link_popup()

    def build_link_popup(self):
        self.found_frame = None
        text = "\n\nSearch for Meal by Name:\n"
        self.search_popup= Toplevel(bg="white")
        self.search_popup.title("Search for Meal by Name")
        
        left_frame = Frame(self.search_popup, width = 40, bg="white")
        left_frame.pack(side=LEFT, fill=Y, padx=(15, 15))
        self.info_icon = Image.open("./images/search_icon.jpg")
        self.info_icon = (self.info_icon).resize((50,50))
        self.info_icon = ImageTk.PhotoImage(self.info_icon)
        self.info_icon_label = Label(left_frame, image=self.info_icon, bg="white")
        self.info_icon_label.pack(anchor='n', padx=0, pady=20)

        Label(self.search_popup, text= text, justify = LEFT, bg="white", wraplength=300).pack(anchor = "n", padx=(10, 40), pady=(0,0))
        self.search_text = StringVar()
        self.search_frame = ttk.Frame(self.search_popup)
        self.search_box = ttk.Entry(self.search_frame, width = 50, textvariable=self.search_text).grid(column=0, row=0)
        self.create_search_button()
        self.search_frame.pack(anchor = "center", padx = (10, 40), pady= (10, 25))
        return

    def display_search_results(self):
        if self.found_frame != None:
            self.found_frame.destroy()
        
        matches = self.get_search_results()

        self.found_frame = ttk.Frame(self.search_frame)
        self.found_frame.grid(column = 0, row = 1, columnspan = 2)

        num_shown = 0
        for match in matches:
            
            if num_shown >= 10:
                break
            found = ttk.Label(self.found_frame, text = match.name.title())
            found.grid(column = 0, row = num_shown)
            self.create_select_button(match, num_shown)
            num_shown = num_shown + 1
        
        if num_shown == 0:
            found = ttk.Label(self.found_frame, text = "No Matches Found")
            found.grid(column = 0, row = num_shown)
    
    def create_select_button(self, meal, index):
        choose_button = ttk.Button(self.found_frame, text = "\u2714", width = 3, command = lambda: self.select_meal(meal))
        choose_button.grid(column = 1, row = index)
        Hovertip(choose_button, "Select this Meal")
    
    def select_meal(self, meal_selection):
        if self.advanced_page == True:
            self.base_page.update_meal_for_search(meal_selection)
        else:
            self.base_page.set_meal_selection(meal_selection)
        self.search_popup.destroy()
    
    def get_search_results(self):
        search_val = self.search_text.get()
        searcher = MealSearcher()
        matches = searcher.search_for_meals(search_val)
        return matches
    
    def create_search_button(self):
        self.search_button = ttk.Button(self.search_frame, text=u"\U0001F50D", width = 3, command=lambda: self.display_search_results())
        self.search_button.grid(column=1, row=0)
        search_tip = Hovertip(self.search_button, "Search")

    def choose_meal(self):
        self.get_search_text()
        self.search_popup.destroy
