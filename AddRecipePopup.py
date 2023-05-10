from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from MultiCheckDropdown import MultiCheckDropdown

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
        
        self.name_frame = Frame(self.right_frame, bg = "white")

        self.add_input_bar("name", self.name_frame)
        self.search_box.grid(column = 0, row = 0)

        self.create_saveoption_button(self.name_frame)
        self.saveoption_button.grid(column = 1, row = 0, padx = (8, 0))

        self.name_frame.pack()
    
    def add_ingredients(self):
        
        Label(self.right_frame, text= "Meal Ingredients: ", bg="white").pack(anchor = "n")
        
        self.ingredients_frame = Frame(self.right_frame, bg="white")
        self.ingredients_frame.pack()
        
        self.add_input_bar("ingredient_names", self.ingredients_frame, "ingredients", 30)
        self.search_box.grid(column = 0, row = 0, padx = (0,19))
        
        self.add_input_bar("ingredient_amounts", self.ingredients_frame, "amount", 10)
        self.search_box.grid(column = 1, row = 0, padx = (19,19))

        self.create_units_dropdown()

        self.create_saveoption_button(self.ingredients_frame)
        self.saveoption_button.grid(column = 3, row = 0, padx = (8, 0))
    
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
        self.add_tag_dropdown()
        self.tag_dropdown.grid(column = 0, row = 1)

        Label(self.tags_frame, text= "Price Range:", bg="white").grid(column = 1, row = 0)
        self.add_pricerange_dropdown()
        self.pricerange_dropdown.grid(column = 1, row = 1, padx = (40,40))

        Label(self.tags_frame, text= "Meal Type:", bg="white").grid(column = 2, row = 0)
        self.add_mealtype_dropdown()
        self.mealtype_dropdown.grid(column = 2, row = 1)
    
    def create_saveoption_button(self, frame):
        self.saveoption_button = ttk.Button(frame, text="\u2795", width = 3, default="active", command= lambda: self.save_option())
    
    def save_option(self):
        pass
    
    def add_tag_dropdown(self):
        dropdown_options = ["Reheats well"]
        self.tag_dropdown = MultiCheckDropdown(self.tags_frame, dropdown_options).display
    
    def add_pricerange_dropdown(self):
        dropdown_options = ["$", "$$", "$$$"]
        self.pricerange_dropdown = MultiCheckDropdown(self.tags_frame, dropdown_options).display

    def add_mealtype_dropdown(self):
        dropdown_options = ["Breakfast", "Lunch", "Dinner"]
        self.mealtype_dropdown = MultiCheckDropdown(self.tags_frame, dropdown_options).display

    def add_link(self):
        Label(self.right_frame, text= "Link", justify = LEFT, bg="white").pack(anchor = "n")
        
        self.link_frame = Frame(self.right_frame, bg="white")
        
        self.add_input_bar("link", self.link_frame)
        self.search_box.grid(column = 0, row = 0)

        self.create_saveoption_button(self.link_frame)
        self.saveoption_button.grid(column = 1, row = 0, padx = (5, 0))

        self.link_frame.pack()

    def add_recipe(self):
        Label(self.right_frame, text= "Recipe", justify = LEFT, bg="white").pack(anchor = "n")
        self.recipe_frame = Frame(self.right_frame, bg="white")
        
        self.recipe_text = Text(self.recipe_frame, height = 10, width = 49, relief = RIDGE, bg = "gray99").grid(column=0, row=0)

        self.create_saveoption_button(self.recipe_frame)
        self.saveoption_button.grid(column = 1, row = 0, padx = (3, 0))

        self.recipe_frame.pack()

    def add_input_bar(self, input_tag, frame, default_text = None, width = 65):
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