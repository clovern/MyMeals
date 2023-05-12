from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from MultiCheckDropdown import MultiCheckDropdown
from Meal import Meal
from MealDatabaseEditor import MealDatabaseEditor

class AddRecipePopup:

    def __init__(self, recipe_book):
        self.input_vars = {"ingredient_names": [], "ingredient_amounts": [], "ingredient_units": []}
        self.recipe_book = recipe_book
        self.ingred_dict = {}
        self.build_addrecipe_popup()

    def build_addrecipe_popup(self):
        self.found_frame = None
        self.addrecipe_popup= Toplevel(bg="white")
        self.addrecipe_popup.title("Add new recipe")

        self.build_footer()

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
    
    def build_footer(self):
        bottom_frame = Frame(self.addrecipe_popup, bg="gray95")
        bottom_frame.pack(side=BOTTOM, fill=X)
        ttk.Button(bottom_frame, text="Save Recipe", width=12, default="active", command=self.save_recipe).pack(anchor='se', pady = (10, 10), padx = 20)

    def add_meal_name(self):
        Label(self.right_frame, text= "Meal Name:", justify = LEFT, bg="white").pack(anchor = "n")
        
        self.name_frame = Frame(self.right_frame, bg = "white")

        self.add_input_bar("name", self.name_frame)
        self.search_box.grid(column = 0, row = 0)

        self.name_frame.pack(padx = (0, 25))
    
    def add_ingredients(self):
        
        Label(self.right_frame, text= "Meal Ingredients: ", bg="white").pack(anchor = "n")
        
        self.ingredients_frame = Frame(self.right_frame, bg="white")
        self.ingredients_frame.pack(padx = (8, 0), pady = (0, 5))
        
        self.ingred_list_frame = Frame(self.right_frame, bg="white")
        self.ingred_list_frame.pack(padx = (8, 0))
        
        self.add_input_bar("ingredient_names", self.ingredients_frame, "ingredients", 30)
        self.search_box.grid(column = 0, row = 0, padx = (0,19))
        
        self.add_input_bar("ingredient_amounts", self.ingredients_frame, "amount", 10)
        self.search_box.grid(column = 1, row = 0, padx = (19,19))

        self.create_units_dropdown()

        self.create_saveoption_button(self.ingredients_frame)
        self.saveoption_button["command"] = lambda: self.add_to_ingredient_list()
        self.saveoption_button.grid(column = 3, row = 0, padx = (8, 0))
    
    def add_to_ingredient_list(self):
        ingred_name = self.input_vars["ingredient_names"].get()
        ingred_amount = self.input_vars["ingredient_amounts"].get()
        ingred_unit = self.units_dropdown.get()
        if ingred_name == "ingredients":
            messagebox.showinfo(title="Error: Invalid Ingredients", message="Please enter a valid value for ingredient name.")
        elif ingred_name in self.ingred_dict:
            messagebox.showinfo(title="Error: Invalid Ingredients", message=ingred_name.title() + " has already been added to your ingredients list. \n\nPlease remove this from your ingredient list first, if you want to change the amount or units.")
        elif ingred_amount == "amount":
            messagebox.showinfo(title="Error: Invalid Ingredients", message="Please enter a valid value for ingredient amount.")
        elif ingred_unit == "units":
            messagebox.showinfo(title="Error: Invalid Ingredients", message="Please select a value for the ingredient units from the dropdown menu.")
        else: 
            self.ingred_dict[ingred_name] = [ingred_amount , ingred_unit]
            display_ingred_frame = Frame(self.ingred_list_frame, bg="white")
            display_ingred_frame.pack()
            self.ingred_label = Label(display_ingred_frame, text= ingred_name + ": " + ingred_amount + " " + ingred_unit, bg="white", borderwidth = 1, relief = SOLID, width = 50)
            self.ingred_label.pack(side = LEFT)
            self.remove_ingred_button = ttk.Button(display_ingred_frame, text="\u2796", width = 3, default="active", command = lambda: self.remove_ingredient(display_ingred_frame, ingred_name))
            self.remove_ingred_button.pack(side = LEFT)

    def remove_ingredient(self, ingred_frame, ingred_name):
        ingred_frame.destroy()
        del self.ingred_dict[ingred_name]

    def create_units_dropdown(self):
        ingred_unit = StringVar()
        self.input_vars["ingredient_units"].append(ingred_unit)
        ttk.Style().configure("Units.TCombobox", foreground = "grey", relief = SUNKEN)
        self.units_dropdown = ttk.Combobox(self.ingredients_frame, style = "Units.TCombobox", width = 10, textvariable = ingred_unit)
        
        self.units_dropdown['values'] = ('unit(s)', 'package(s)', 'cup(s)', 'Tbsp(s)', 'tsp(s)', 'oz(s)', 'gram(s)', 'lb(s)', 'ml(s)', 'Liter(s)')
        self.units_dropdown.set("units")
        self.units_dropdown.grid(column = 2, row = 0, padx = (2,2))
        
    def add_tags(self):
        self.tags_frame = Frame(self.right_frame, bg="white")
        self.tags_frame.pack(padx = (0, 25))

        Label(self.tags_frame, text= "Tags:", bg="white").grid(column = 0, row = 0)
        self.add_tag_dropdown()
        self.tag_dropdown.display.grid(column = 0, row = 1)

        Label(self.tags_frame, text= "Price Range:", bg="white").grid(column = 1, row = 0)
        self.add_pricerange_dropdown()
        self.pricerange_dropdown.grid(column = 1, row = 1, padx = (20,20))

        Label(self.tags_frame, text= "Meal Type:", bg="white").grid(column = 2, row = 0, padx = (0, 20))
        self.add_mealtype_dropdown()
        self.mealtype_dropdown.grid(column = 2, row = 1, padx = (0, 20))

        Label(self.tags_frame, text= "Meat Type:", bg="white").grid(column = 3, row = 0)
        self.add_meattype_dropdown()
        self.meattype_dropdown.grid(column = 3, row = 1)
    
    def create_saveoption_button(self, frame):
        self.saveoption_button = ttk.Button(frame, text="\u2795", width = 3, default="active")
    
    def add_tag_dropdown(self):
        dropdown_options = ["Reheats well"]
        self.tag_dropdown = MultiCheckDropdown(self.tags_frame, dropdown_options)
    
    def add_pricerange_dropdown(self):

        pricerange_unit = StringVar()
        self.pricerange_dropdown = ttk.Combobox(self.tags_frame, width = 10, textvariable = pricerange_unit)
        
        self.pricerange_dropdown['values'] = ("$", "$$", "$$$")

    def add_meattype_dropdown(self):

        meattype_unit = StringVar()
        self.meattype_dropdown = ttk.Combobox(self.tags_frame, width = 10, textvariable = meattype_unit)
        
        self.meattype_dropdown['values'] = ("Vegan", "Vegetarian", "Chicken", "Pork", "Beef", "Turkey", "Seafood")
    
    def add_mealtype_dropdown(self):

        mealtype_unit = StringVar()
        self.mealtype_dropdown = ttk.Combobox(self.tags_frame, width = 10, textvariable = mealtype_unit)
        
        self.mealtype_dropdown['values'] = ("Breakfast", "Lunch", "Dinner")

    def add_link(self):
        Label(self.right_frame, text= "Link", justify = LEFT, bg="white").pack(anchor = "n")
        
        self.link_frame = Frame(self.right_frame, bg="white")
        
        self.add_input_bar("link", self.link_frame)
        self.search_box.grid(column = 0, row = 0)

        self.link_frame.pack(padx = (0, 25))

    def add_recipe(self):
        Label(self.right_frame, text= "Recipe", justify = LEFT, bg="white").pack(anchor = "n")
        self.recipe_frame = Frame(self.right_frame, bg="white")
        
        self.recipe_text = Text(self.recipe_frame, height = 10, width = 49, relief = RIDGE, bg = "gray99")
        self.recipe_text.grid(column=0, row=0)

        self.recipe_frame.pack(padx = (0, 25))

    def add_input_bar(self, input_tag, frame, default_text = None, width = 65):
        search_text = StringVar()
        self.search_box = Entry(frame, width = width, textvariable=search_text, fg="grey")
        self.input_vars[input_tag] = self.search_box
        if default_text != None:
            self.search_box.insert(0, default_text)

    def confirm_delete(self):
        self.addrecipe_popup.destroy()

    def save_recipe(self):
        name = self.input_vars["name"].get()
        meat_type = self.meattype_dropdown.get()
        reheats_well = "true" if "Reheats well" in self.tag_dropdown.get_selected_opts() else "false"
        price_range = self.get_price_range()
        meal_type = self.mealtype_dropdown.get()
        recipe = self.recipe_text.get("1.0",'end-1c')
        if recipe == "":
            recipe = None
        link = self.input_vars["link"].get()
        if link == "":
            link = None
        ingredients = self.ingred_dict
        vegan_only = "false"
        
        meal_vars = {
            "name": name,
            "meat_type": meat_type,
            "meal_type": meal_type,
            "recipe": recipe,
            "link": link,
            "ingredients": ingredients
        }

        if self.verify_meal(meal_vars) == False:
            self.addrecipe_popup.lift()
            return

        newmeal = Meal(name, meat_type, reheats_well, price_range, meal_type, recipe, link, vegan_only, ingredients)
        self.recipe_book.add_meal(newmeal)
        messagebox.showinfo(title="Meal Successfully Added", message= name.title() + " has been successfully added to your recipe list!")
        self.addrecipe_popup.lift()
        self.addrecipe_popup.destroy()

    def show_error_message(self, message):
        messagebox.showinfo(title="Error", message=message)
    
    def get_price_range(self):
        price_range = self.pricerange_dropdown.get()
        if price_range == "$" or price_range == None:
            price_range = "cheap"
        elif price_range == "$$":
            price_range = "medium"
        elif price_range == "$$$":
            price_range = "expensive"
        return price_range
    
    def verify_meal(self, meal_vars):
        if meal_vars["name"] == "":
            self.show_error_message("Meal name is required. Please add a name, then save your recipe")
            return False

        if meal_vars["meat_type"] == None or meal_vars["meat_type"] == "":
            self.show_error_message("Meat type is required. Please add a meat type, then save your recipe")
            return False
        
        if meal_vars["meal_type"] == None or meal_vars["meal_type"] == "":
            self.show_error_message("Meal type is required. Please add a meal type, then save your recipe")
            return False

        if meal_vars["link"] == None and meal_vars["recipe"] == None:
            norecipe_response = messagebox.askyesno(title="Verify", message="This meal does not have a recipe or a recipe link added. Are you sure you want to save it without any recipe information?")

            if norecipe_response == False:
                return False
        if len(meal_vars["ingredients"]) == 0:
            ingred_response = messagebox.askyesno(title="Verify", message="This meal does not have any added ingredients. Are you sure you want to save it without ingredients?")
            if ingred_response ==False:
                return False
        
        return True
