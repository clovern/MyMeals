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
        self.centerInFrame()
    
    def addQuestions(self):
        self.mealQuestionPrompt("breakfasts")
        self.mealQuestionPrompt("lunches")
        self.mealQuestionPrompt("dinners")
        self.specialOptionsPrompt()
    
    def mealQuestionPrompt(self, meal):
        self.questionFrame= ttk.Frame(self.lowercontent)
        self.questionFrame['padding'] = (20, 20, 20, 20)
        mealQuestion = 'How many {0} would you like planned this week?'.format(meal)
        self.mealQuestionLabel = ttk.Label(self.questionFrame, text=mealQuestion, font=("Arial", 15))
        self.createNumberDropdown()

        index = 0
        if (meal == "lunches"): index = 1
        elif (meal == "dinners"): index = 2

        self.mealQuestionLabel.grid(column=0, row=0, columnspan=3)
        self.basicDropdown.grid(column=2, row=1)
        self.questionFrame.grid(column=0, row=index)
    
    def createSubmitButton(self):
        super().createSubmitButton()
        self.submitButton.grid(column=0, columnspan=3, row=4)
    
    def createNumberDropdown(self):
        self.choiceSelection = StringVar()
        self.basicDropdown = ttk.Combobox(self.questionFrame, textvariable=self.choiceSelection)
        self.basicDropdown['values'] = (
                            '0',
                            '1',
                            '2',
                            '3',
                            '4',
                            '5',
                            '6',
                            '7')
        self.basicDropdown.current(0)

    def centerInFrame(self):
        pass
    
    def specialOptionsPrompt(self):
        self.questionFrame= ttk.Frame(self.lowercontent)
        self.mealQuestionLabel = ttk.Label(self.questionFrame, text="Special options?", font=("Arial", 15))
        self.createSpecialOptionsDropdown(self.questionFrame)

        self.mealQuestionLabel.grid(column=0, row=0, columnspan = 3, sticky='E')
        self.specialDropdown.grid(column=2, row=1)
        self.questionFrame.grid(column=0, row=3)
        

    def generatePlan(self):
        pass

