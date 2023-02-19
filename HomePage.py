from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from AdvancedPlanPage import AdvancedPlanPage
from BasicPlanPage import BasicPlanPage

class HomePage:
    def __init__(self, root):
        root.title("MyMeals")
        self.createOuterFrame()
        self.createInnerFrame()
        self.populateWidgets()
        self.setWidgetGrid()

    def createOuterFrame(self):
        self.outer = ttk.Frame(root, height=800, width=800)
        self.outer.grid_propagate(0)
        self.outer.pack()

    def createInnerFrame(self):
        self.content = ttk.Frame(self.outer)
        self.content['padding'] = (40,40,40,40)
        self.content.grid(column=0, row=0)
        self.outer.columnconfigure(0, weight=1)
        self.outer.rowconfigure(0, weight=1)

    def populateWidgets(self):
        self.welcomeLabel = ttk.Label(self.content, text = "Welcome to MyMeals!")
        self.instructionLabel = Label(self.content, text = "Get dinners in one click with the basic plan creator, or customize your \n \
        preferences with the advanced planner.")
        self.basicPlanButton = ttk.Button(self.content, text='Create Basic Plan', command=self.basicPlan)
        self.advancedPlanButton = ttk.Button(self.content, text='Create Advanced Plan', command=self.advancedPlan)

        self.logoImage = Image.open("./MyMealsLogo.png")
        self.logoImage = (self.logoImage).resize((500,500))
        self.logoImage = ImageTk.PhotoImage(self.logoImage)
        self.logoImageLabel = ttk.Label(self.content, image=self.logoImage)

    def setWidgetGrid(self):
        self.logoImageLabel.grid(column=1, row=0, columnspan = 2, padx=20, pady=10)
        self.welcomeLabel.grid(column=1, row=1, columnspan=2)
        self.instructionLabel.grid(column=0, row=2, columnspan=4, padx=20, pady=10)
        self.basicPlanButton.grid(column=1, row=3)
        self.advancedPlanButton.grid(column=2, row=3)

    def basicPlan(self):
        self.clearPage()
        basicPlanPage = BasicPlanPage(root)
        return
    
    def advancedPlan(self):
        self.clearPage()
        advancedPlanPage = AdvancedPlanPage(root)
        return
    
    def clearPage(self):
        self.content.destroy()


root = Tk()
homepage = HomePage(root)
root.mainloop()
