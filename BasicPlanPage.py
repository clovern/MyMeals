from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage

class BasicPlanPage(PlanPage):
    def __init__(self, root, outer):
        self.outer = outer
        self.createBasicPlanDisplay()
    
    def createBasicPlanDisplay(self):
        self.createUpperFrame()
        self.createLowerFrame()
        self.createTitle("Basic Plan Creator")
        self.addQuestions()
        self.createSubmitButton()
    
    def addQuestions(self):
        self.mealQuestionPrompt("breakfasts")
        self.mealQuestionPrompt("lunches")
        self.mealQuestionPrompt("dinners")
        self.specialOptionsPrompt()
    
    def mealQuestionPrompt(self, meal):
        mealQuestion = 'How many {0} would you like planned this week?'.format(meal)
        self.mealQuestionLabel = ttk.Label(self.lowercontent, text=mealQuestion, font=("Arial", 15))

        index = 0
        if (meal == "lunches"): index = 1
        elif (meal == "dinners"): index = 2

        self.mealQuestionLabel.grid(column=0, row=index, columnspan = 3)
    
    def createSubmitButton(self):
        super().createSubmitButton()
        self.submitButton.grid(column=0, columnspan=3, row=3)

    
    def specialOptionsPrompt(self):
        pass

    def generatePlan(self):
        pass

