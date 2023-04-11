from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from PlanPage import PlanPage
from MealInfoDisplay import MealInfoDisplay

class BasicPlanPage(PlanPage):
    def __init__(self, root, outer):
        self.outer = outer
        super().__init__()
        self.dropdownList = []

        self.createBasicPlanDisplay()
    
    def createBasicPlanDisplay(self):
        self.createUpperFrame()
        self.createLowerFrame()
        self.centerInFrame()
        self.createTitle("Basic Plan Creator")
        self.addQuestions()
        self.createSubmitButton()
    
    def addQuestions(self):
        self.createMealQuestionPrompt("breakfasts")
        self.createMealQuestionPrompt("lunches")
        self.createMealQuestionPrompt("dinners")
        self.specialOptionsPrompt()
        self.setDropdownDefaults()
    
    def createMealQuestionPrompt(self, meal):
        self.questionFrame= ttk.Frame(self.lowercontent)
        self.questionFrame['padding'] = (15, 15, 15, 15)
        mealQuestion = 'How many {0} would you like planned this week?'.format(meal)
        self.mealQuestionLabel = ttk.Label(self.questionFrame, text=mealQuestion, font=("Arial", 15))
        self.createNumberDropdown()

        index = 0
        if (meal == "lunches"): index = 1
        elif (meal == "dinners"): index = 2

        self.mealQuestionLabel.grid(column=0, row=0, columnspan=3, sticky='E')
        (self.dropdownList[-1]).grid(column=2, row=1, sticky='E', pady= (2,2))
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
        self.dropdownList.append(self.basicDropdown)

    def centerInFrame(self):
        self.lowercontent.grid_columnconfigure(0, weight=1)
    
    def specialOptionsPrompt(self):
        self.questionFrame= ttk.Frame(self.lowercontent, width=600)
        self.questionFrame['padding'] = (15, 15, 15, 15)

        self.mealQuestionLabel = ttk.Label(self.questionFrame, text="Special options?", font=("Arial", 15))
        self.createSpecialOptionsDropdown(self.questionFrame)

        self.mealQuestionLabel.grid(column=0, row=0, columnspan = 3, sticky='E')
        self.specialDropdown.display.grid(column=2, row=1, pady = (2, 2))
        self.questionFrame.grid(column=0, row=3)
    
    def setDropdownDefaults(self):
        self.dropdownList[0].current(7)
        self.dropdownList[1].current(7)
        self.dropdownList[2].current(7)

    def generatePlan(self):

        super().generatePlan()

        self.meal_creator.setWeeklyPreferencesBasic(self.dropdownList, self.specialDropdown)
        self.meal_creator.create_meal_plan()

        self.clearPage()
        displayMealPage = MealInfoDisplay(self.outer, self.meal_creator)
        

