from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from abc import ABC, abstractmethod
from SpecialOptionsDropdown import SpecialOptionsDropdown
from MealCreator import MealCreator

class MealInfoDisplay:
    def __init__(self, root):
        root.title("MyMeals")
        self.createUpperFrame

    def createUpperFrame(self):
        self.uppercontent= ttk.Frame(self.outer)
        self.uppercontent.grid(column=0, row=0)
    
    def createLowerFrame(self):
        self.lowercontent = ttk.Frame(self.outer, height=600, width=800)
        self.lowercontent.grid(column=0, row=1)
        self.lowercontent.grid_propagate(0)

    # FIXME implement
    def createNavBar(self):
        pass

    def createTitle(self, titleText):

        self.logoImage = Image.open("./MyMealsLogo.png")
        self.logoImage = (self.logoImage).resize((150,150))
        self.logoImage = ImageTk.PhotoImage(self.logoImage)
        self.logoImageLabel = ttk.Label(self.uppercontent, image=self.logoImage)
        # below line resolves tkinter bug with saving image files
        self.logoImageLabel.image = self.logoImage
        self.logoImageLabel.grid(column=0, row=0)


        self.title = ttk.Label(self.uppercontent, text=titleText, font=("Arial", 25))
        self.title['padding'] = (40, 40, 40, 40)
        self.title.grid(column=1, row=0)

    def createSubmitButton(self):
        self.submitButton = ttk.Button(self.lowercontent, text="Create Plan", default="active", command=self.generatePlan)

    def createSpecialOptionsDropdown(self, frame):
        self.specialDropdown = SpecialOptionsDropdown(frame) 

    def generatePlan(self):
        self.meal_creator = MealCreator()
    
    def clearPage(self):
        self.uppercontent.destroy()
        self.lowercontent.destroy()