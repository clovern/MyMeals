from Implementation.MealPlanCreator import MealPlanCreator

class MealSearcher:

    def __init__(self):
        self.meal_creator = MealPlanCreator()
    
    def search_for_meals(self, search_text):
        self.meals_found = []
        meal_options = self.meal_creator.all_meals

        for meal in meal_options:
            if search_text.lower() in meal.name.lower():
                self.meals_found.append(meal)
        
        return self.meals_found

    
