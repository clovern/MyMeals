class Meal: 
    def __init__(self, name, meat_type, reheats_well, price_range, meal_type, ingredients = {}):
        self.name = name
        self.meat_type = meat_type
        self.reheats_well = reheats_well
        self.price_range = price_range
        self.meal_type = meal_type
        self.ingredients = ingredients

    def add_ingredient(self, ingredient, amount):
        self.ingredients[ingredient] = str(amount)     

    def __repr__(self):
        return self.name


    