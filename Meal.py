class Meal: 
    def __init__(self, name, meat_type, reheats_well, price_range, meal_type, ingredients = {}, recipe = None, link = None):
        self.name = name
        self.meat_type = meat_type
        self.reheats_well = reheats_well
        self.price_range = price_range
        self.meal_type = meal_type
        self.ingredients = ingredients
        self.recipe = recipe
        self.link = link

    def add_ingredient(self, ingredient, amount):
        self.ingredients[ingredient] = str(amount)   

    def ingredients_to_string_list(self):
        ingredients_list = []
        for ingredient in self.ingredients.keys():
            ingredient_string = ingredient + ", " 
            ingredient_amounts_list = self.ingredients[ingredient]
            for measurement in ingredient_amounts_list:
                ingredient_string += " " + measurement
            ingredients_list.append(ingredient_string)
        
        return ingredients_list

    def __repr__(self):
        return self.name


    