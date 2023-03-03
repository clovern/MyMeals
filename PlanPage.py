from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from abc import ABC, abstractmethod

class PlanPage(ABC):
    def __init__(self, root):
        root.title("MyMeals")
        self.createUpperFrame()
        self.createLowerFrame()

    def createUpperFrame(self):
        self.uppercontent= ttk.Frame(self.outer)
        self.uppercontent.grid(column=0, row=0)
    
    def createLowerFrame(self):
        self.lowercontent = Frame(self.outer, background = "Blue")
        self.lowercontent.grid(column=0, row=1)

    # FIXME implement
    def createNavBar(self):
        pass

    # FIXME implement
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

    # FIXME implement
    def createPlanButton():
        pass

    # FIXME implement
    def generatePlan():
        pass

    @abstractmethod
    def populateWidgets(self):
        ...

    @abstractmethod
    def setWidgetGrid(self):
        ...
    
    def clearPage(self):
        self.uppercontent.destroy()
        self.lowercontent.destroy()