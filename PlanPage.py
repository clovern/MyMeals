from tkinter import *
from tkinter import ttk
from SpecialOptionsDropdown import SpecialOptionsDropdown
from MealCreator import MealCreator
from Page import Page

class PlanPage(Page):
    def __init__(self):
        self.createUpperFrame()
        self.createLowerFrame()
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def createSubmitButton(self):
        self.submitButton = ttk.Button(self.lowercontent, text="Create Plan", default="active", command=self.generatePlan)

    def createSpecialOptionsDropdown(self, frame):
        self.specialDropdown = SpecialOptionsDropdown(frame)

    def generatePlan(self):
        self.meal_creator = MealCreator()
    
    def createAllDays(self):
        index = 0
        for day in self.days:
            self.createDayPanel(day, index)
            index += 1
    
    def createDayFlag(self, day):
        self.dayFlag = ttk.Label(self.dayFrame, text=day, width=10, font=("Arial", 15))
        self.dayFlag.grid(column=0, row=0)
    
    def createDayPanel(self, day, index):
        if (index < 4):
            self.dayFrame= ttk.Frame(self.lowerLeftContent)
        else:
            self.dayFrame= ttk.Frame(self.lowerRightContent)
            index -= 4
        
        self.dayFrame['padding'] = (10, 10, 10, 10)
        self.dayFrame.grid(column=0, row=index)
        self.createDayFlag(day)