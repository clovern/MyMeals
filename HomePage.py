from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from AdvancedPlanPage import AdvancedPlanPage
from BasicPlanPage import BasicPlanPage
from MealListDisplay import MealListDisplay
# FIXME
from MealDatabaseEditor import MealDatabaseEditor

class HomePage:
    def __init__(self, root):
        root.title("MyMeals")
        self.create_outer_frame()
        self.create_inner_frame()
        self.populate_widgets()

    def create_outer_frame(self):
        self.outer = ttk.Frame(root, height=800, width=800)
        self.outer.grid_propagate(0)
        self.outer.grid(column=0, row=0)

    def create_inner_frame(self):
        self.content = ttk.Frame(self.outer)
        self.content['padding'] = (40,40,40,40)
        self.content.grid(column=0, row=0)
        self.outer.columnconfigure(0, weight=1)
        self.outer.rowconfigure(0, weight=1)

    def populate_widgets(self):
        self.create_welcome_label()
        self.create_instruction_label()
        self.create_option_buttons()

        self.logo_image = Image.open("./my_meals_logo.png")
        self.logo_image = (self.logo_image).resize((500,500))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_image_label = ttk.Label(self.content, image=self.logo_image)
        self.logo_image_label.grid(column=1, row=0, columnspan = 2, padx=20, pady=10)

    def create_welcome_label(self):
        self.welcome_label = ttk.Label(self.content, text = "Welcome to MyMeals!")
        self.welcome_label.grid(column=1, row=1, columnspan=2)
    
    def create_instruction_label(self):
        self.instruction_label = Label(self.content, text = "Get dinners in one click with the basic plan creator, or customize your \n \
        preferences with the advanced planner.")
        self.instruction_label.grid(column=0, row=2, columnspan=4, padx=20, pady=10)
    
    def create_option_buttons(self):
        self.create_button_frame()
        self.create_basicplan_button()
        self.create_advancedplan_button()
        self.create_viewmeals_button()
    
    def create_button_frame(self):
        self.buttonframe = ttk.Frame(self.content)
        self.buttonframe.grid(column = 1, row = 3, columnspan = 2)

    def create_basicplan_button(self):
        self.basic_plan_button = ttk.Button(self.buttonframe, text='Create Basic Plan', command=self.basic_plan)
        self.basic_plan_button.grid(column=0, row = 0, padx = (25, 25))

    def create_advancedplan_button(self):
        self.advanced_plan_button = ttk.Button(self.buttonframe, text='Create Advanced Plan', command=self.advanced_plan)
        self.advanced_plan_button.grid(column=1, row=0, padx = (25, 25))

    def create_viewmeals_button(self):
        text = u"\U0001F56E"
        text += " Recipe Book"
        self.viewmeals_button = ttk.Button(self.buttonframe, text=text, command=self.view_recipes)
        self.viewmeals_button.grid(column=2, row=0, padx = (25, 25))

    def basic_plan(self):
        self.clear_page()
        basic_plan_page = BasicPlanPage(root, self.outer, self.content)
        return
    
    def advanced_plan(self):
        self.clear_page()
        advanced_plan_page = AdvancedPlanPage(root, self.outer, self.content)
        return

    def view_recipes(self):
        self.clear_page()
        MealListDisplay(self.outer, self.content)
    
    def clear_page(self):
        self.content.grid_forget()

def start_GUI():
    global root 
    root = Tk()
    # FIXME
    MealDatabaseEditor.populate_default_meals()
    MealDatabaseEditor.remove_meal("vegan blueberry waffles")
    homepage = HomePage(root)
    root.mainloop()
