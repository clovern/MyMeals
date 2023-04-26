from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
import webbrowser
from PIL import Image
from PIL import ImageTk
from idlelib.tooltip import Hovertip
from MealSearcher import MealSearcher

class MealSearcherPopup:

    # def __init__(self, mealday, meal, label):
    def __init__(self):
        # self.mealday = mealday
        # self.meal = meal
        # self.label = label
        self.build_link_popup()

    def build_link_popup(self):
        self.found_frame = None
        text = "\n\nSearch for Meal by Name:\n"
        self.search_popup= Toplevel(bg="white")
        self.search_popup.title("Search for Meal by Name")
        
        # bottom_frame = Frame(self.search_popup, bg="gray95")
        # bottom_frame.pack(side=BOTTOM, fill=X)
        # ttk.Button(bottom_frame, text="Select this meal", width=20, default="active", command=self.choose_meal).pack(anchor='se', pady = 10, padx = 15)
        
        left_frame = Frame(self.search_popup, width = 40, bg="white")
        left_frame.pack(side=LEFT, fill=Y, padx=(15, 15))
        self.info_icon = Image.open("./search_icon.jpg")
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
    
    def create_select_button(self, meal, index):
        choose_button = ttk.Button(self.found_frame, text = "\u2714", width = 3, command = lambda: self.select_meal(meal))
        choose_button.grid(column = 1, row = index)
        Hovertip(choose_button, "Select this Meal")
    
    def select_meal(self, meal):
        # FIXME
        print("SELECTED " + meal.name)
    
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
