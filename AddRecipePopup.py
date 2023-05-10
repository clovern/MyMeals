from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from SpecialOptionsDropdown import SpecialOptionsDropdown

class AddRecipePopup:

    def __init__(self, recipe_book):
        self.input_vars = {"ingredient_names": [], "ingredient_amounts": [], "ingredient_units": []}
        self.recipe_book = recipe_book
        self.build_addrecipe_popup()

    def build_addrecipe_popup(self):
        self.found_frame = None
        self.addrecipe_popup= Toplevel(bg="white")
        self.addrecipe_popup.title("Add new recipe")

        left_frame = Frame(self.addrecipe_popup, width = 40, bg="white")
        left_frame.pack(side=LEFT, fill=Y, padx=(15, 15))
        self.info_icon = Image.open("./add_meals.png")
        self.info_icon = (self.info_icon).resize((50,50))
        self.info_icon = ImageTk.PhotoImage(self.info_icon)
        self.info_icon_label = Label(left_frame, image=self.info_icon, bg="white")
        self.info_icon_label.pack(anchor='n', padx=0, pady=20)

        self.right_frame = Frame(self.addrecipe_popup, bg="white")
        self.right_frame.pack(side=RIGHT, padx = (0, 20), pady = (0, 20))

        self.add_meal_name()
        self.add_ingredients()
        self.add_tags()
        self.add_link()
        self.add_recipe()

    def add_meal_name(self):
        Label(self.right_frame, text= "Meal Name:", justify = LEFT, bg="white").pack(anchor = "n")
        self.add_input_bar("name", self.right_frame)
        self.search_box.pack()
    
    def add_ingredients(self):
        Label(self.right_frame, text= "Meal Ingredients: ", bg="white").pack(anchor = "n")
        self.ingredients_frame = Frame(self.right_frame, bg="white")
        self.ingredients_frame.pack()
        self.add_input_bar("ingredient_names", self.ingredients_frame, "ingredients", 30)
        self.search_box.grid(column = 0, row = 0, padx = (2,2))
        self.add_input_bar("ingredient_amounts", self.ingredients_frame, "amount", 10)
        self.search_box.grid(column = 1, row = 0, padx = (2,2))
        self.create_units_dropdown()
    
    def create_units_dropdown(self):
        ingred_unit = StringVar()
        self.input_vars["ingredient_units"].append(ingred_unit)
        ttk.Style().configure("Units.TCombobox", foreground = "grey", relief = SUNKEN)
        units_dropdown = ttk.Combobox(self.ingredients_frame, style = "Units.TCombobox", width = 10, textvariable = ingred_unit)
        
        units_dropdown['values'] = ('unit(s)', 'package(s)', 'cup(s)', 'Tbsp(s)', 'tsp(s)', 'oz(s)', 'gram(s)', 'lb(s)', 'ml(s)', 'Liter(s)')
        units_dropdown.set("units")
        units_dropdown.grid(column = 2, row = 0, padx = (2,2))
        
    def add_tags(self):
        self.tags_frame = Frame(self.right_frame, bg="white")
        self.tags_frame.pack()

        Label(self.tags_frame, text= "Tags:", bg="white").grid(column = 0, row = 0)
        self.add_input_bar("tags", self.tags_frame, width = 10)
        self.search_box.grid(column = 0, row = 1, padx = (2,2))

        Label(self.tags_frame, text= "Price Range:", bg="white").grid(column = 1, row = 0)
        self.add_input_bar("price_range", self.tags_frame, width = 10)
        self.search_box.grid(column = 1, row = 1, padx = (2,2))

        Label(self.tags_frame, text= "Meal Type:", bg="white").grid(column = 2, row = 0)
        self.add_input_bar("meal_type", self.tags_frame, width = 10)
        self.search_box.grid(column = 2, row = 1, padx = (2,2))

    def add_link(self):
        Label(self.right_frame, text= "Link", justify = LEFT, bg="white").pack(anchor = "n")
        self.add_input_bar("link", self.right_frame)
        self.search_box.pack()

    def add_recipe(self):
        Label(self.right_frame, text= "Recipe", justify = LEFT, bg="white").pack(anchor = "n")
        self.recipe_text = Text(self.right_frame, height = 10, width = 50, relief = RIDGE, bg = "gray99").pack()

    def add_input_bar(self, input_tag, frame, default_text = None, width = 50):
        search_text = StringVar()
        if input_tag in ["ingredient_names", "ingredient_amounts", "ingredient_units"]:
            self.input_vars[input_tag].append(search_text)
        else:
            self.input_vars[input_tag] = search_text
        self.search_box = Entry(frame, width = width, textvariable=search_text, fg="grey")
        if default_text != None:
            self.search_box.insert(0, default_text)

    def confirm_delete(self):
        self.addrecipe_popup.destroy()