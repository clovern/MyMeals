from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from abc import ABC, abstractmethod

class Page(ABC):
    def __init__(self, root):
        root.title("MyMeals")

    def createUpperFrame(self):
        self.uppercontent= ttk.Frame(self.outer)
        self.uppercontent.grid(column=0, row=0)
    
    def createLowerFrame(self):
        self.lowercontent = ttk.Frame(self.outer, height=600, width=800)
        self.lowercontent.grid(column=0, row=1)
        self.lowercontent.grid_propagate(0)
    
    def createLowerLeftFrame(self):
        self.lowerLeftContent = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lowerLeftContent.grid(column=0, row=0)
        self.lowerLeftContent.grid_propagate(0)
    
    def createLowerRightFrame(self):
        self.lowerRightContent = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lowerRightContent.grid(column=1, row=0)
        self.lowerRightContent.grid_propagate(0) 

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
    
    def clearPage(self):
        self.uppercontent.destroy()
        self.lowercontent.destroy()