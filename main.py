from MealCreator import MealCreator
from Meal import Meal
from MealDay import MealDay
from HomePage import MealGUI
import json


def populate_default_meals(meal_creator):
    #read from a json file of default meals. Returns as dictionary
    default_file = open('default_meals.json')
    default_data = json.load(default_file)

    #create a meal object for each meal read
    for recipe in default_data:
        temp_meal = Meal(recipe['meal_name'], recipe['meat_type'], recipe['reheats_well'], recipe['price_range'], recipe['meal_type'], recipe['ingredients'])
        meal_creator.add_meal(temp_meal)
    default_file.close()
    return

#FIXME this should later be automated based on the GUI
def set_mealday_preferences():
    mealdays_array = [MealDay("Monday"), MealDay("Tuesday"), MealDay("Wednesday"), MealDay("Thursday"), MealDay("Friday"), MealDay("Saturday"), MealDay("Sunday")]

    for mealday in mealdays_array:
        mealday.add_options("breakfast")
        mealday.add_options("lunch")
        mealday_dinner_options = {'meat_type': 'vegan'}
        mealday.add_options("dinner", mealday_dinner_options)
    return mealdays_array
        

#meals currently created with size for 2 people
def main():
    meal_creator = MealCreator()
    populate_default_meals(meal_creator)

    #have option to select basic meal plan
    #take in options
    #have option to select advanced meal plan and set options
    #take in options

    #sets preferences for Breakfast, Lunch, and Dinner based on input from the GUI
    mealdays_array = set_mealday_preferences()

    # #FIXME TESTING
    # for mealday in mealdays_array:
    #     print('Options')
    #     print(mealday.breakfast_opts)
    #     print(mealday.lunch_opts)
    #     print(mealday.dinner_opts)
    #     print()
    
    #chooses options for breakfast, lunch, and dinner based on advanced options. 
    meal_creator.create_advanced_plan(mealdays_array)
    for mealday in mealdays_array:
        print(mealday.day + ":")
        if (mealday.breakfast_choice != None): 
            print("Breakfast: " + str(mealday.breakfast_choice))
        if (mealday.lunch_choice != None): 
            print("Lunch: " + str(mealday.lunch_choice))
        if (mealday.dinner_choice != None): 
            print("Dinner: " + str(mealday.dinner_choice))
        print()

    #instead I should output the meal plan and the ingredients list to a file.
    #But this functionality should probably be in a separate function. 
    for meal in (meal_creator.create_basic_plan(4)):
        print(meal)
    
    print()

    for meal in (meal_creator.create_basic_plan(4)):
        print(meal)

    gui = MealGUI()
    gui.start_gui
    

        
    


    


    
if __name__ == 'main':
    main()

main()