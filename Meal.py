class Meal: 
    def __init__(self, name, meat_type, reheats_well, price_range, meal_type, recipe, link, vegan_only, ingredients = {}):
        self.name = name
        self.meat_type = meat_type
        self.reheats_well = reheats_well
        self.price_range = price_range
        self.meal_type = meal_type
        self.ingredients = ingredients
        self.recipe = recipe
        self.link = link
        self.vegan_only = vegan_only

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
    
    def format_meal_ingredients(self):
        ingredients_list = self.ingredients_to_string_list()
        information = "Ingredients: \n\n"

        for ingredient in ingredients_list:
            information += ingredient + "\n"
        
        return information

    def format_link_or_recipe_text(self):

        output = ""
        line_length = 75

        if self.link != None:
            output += "Recipe Link: \n\n"
            link_wrapped_array = [(self.link[i: i+line_length]) for i in range(0, len(self.link), line_length)]
            
            for line in link_wrapped_array:
                output = output + line + "\n" 

        elif self.recipe != None:
            output += "Recipe Instructions: \n\n"

            paragraphs_array = self.recipe.split('\n')
            
            for paragraph in paragraphs_array:

                temp_length = min(len(paragraph), line_length)
                if temp_length == 0:
                    temp_length = 1
                recipe_lines_array = [(paragraph[i: i+temp_length]) for i in range(0, len(paragraph), temp_length)]

                for line in recipe_lines_array:
                    output = output + line + "\n" 
            
        else:
            output = "Recipe: \n\nNo recipe or link provided"
        
        return output

    def __repr__(self):
        return self.name


    