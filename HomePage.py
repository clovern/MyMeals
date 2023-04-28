from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from AdvancedPlanPage import AdvancedPlanPage
from BasicPlanPage import BasicPlanPage

class HomePage:
    def __init__(self, root):
        root.title("MyMeals")
        self.create_outer_frame()
        self.create_inner_frame()
        self.populate_widgets()
        self.set_widget_grid()

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
        self.welcome_label = ttk.Label(self.content, text = "Welcome to MyMeals!")
        self.instruction_label = Label(self.content, text = "Get dinners in one click with the basic plan creator, or customize your \n \
        preferences with the advanced planner.")
        self.basic_plan_button = ttk.Button(self.content, text='Create Basic Plan', command=self.basic_plan)
        self.advanced_plan_button = ttk.Button(self.content, text='Create Advanced Plan', command=self.advanced_plan)

        self.logo_image = Image.open("./my_meals_logo.png")
        self.logo_image = (self.logo_image).resize((500,500))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_image_label = ttk.Label(self.content, image=self.logo_image)

    def set_widget_grid(self):
        self.logo_image_label.grid(column=1, row=0, columnspan = 2, padx=20, pady=10)
        self.welcome_label.grid(column=1, row=1, columnspan=2)
        self.instruction_label.grid(column=0, row=2, columnspan=4, padx=20, pady=10)
        self.basic_plan_button.grid(column=1, row=3)
        self.advanced_plan_button.grid(column=2, row=3)

    def basic_plan(self):
        self.clear_page()
        basic_plan_page = BasicPlanPage(root, self.outer, self.content)
        return
    
    def advanced_plan(self):
        self.clear_page()
        advanced_plan_page = AdvancedPlanPage(root, self.outer, self.content)
        return
    
    def clear_page(self):
        self.content.grid_forget()

def start_GUI():
    global root 
    root = Tk()
    homepage = HomePage(root)
    root.mainloop()
