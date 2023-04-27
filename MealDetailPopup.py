from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser
from PIL import Image
from PIL import ImageTk

class MealDetailPopup:

    def __init__(self, mealday, meal):
        self.mealday = mealday
        self.meal = meal
        self.show_meal_details()

    def show_meal_details(self):
        # open a message box that shows the ingredients and the recipe

        meal_choice = self.mealday.get_choice(self.meal)

        information = meal_choice.format_meal_ingredients()
        
        if meal_choice.link != None:
            self.build_link_popup(information, meal_choice)
            return
        
        if meal_choice.recipe != None:
            information += "\n\nRecipe: \n\n"
            information += meal_choice.recipe
            information += "\n"

        messagebox.showinfo("Details for " + meal_choice.name.title(), information)
    def open_hyperlink(self, url):
        webbrowser.open_new_tab(url)

    #Create a Label to display the link
    def create_hyperlink(self, link_text):
        link = Label(self.details_popup, text=link_text, fg="blue", cursor="hand2", bg="white", wraplength=300, justify=LEFT)
        link.bind("<Button-1>", lambda e:
        self.open_hyperlink(link_text))
        link.pack(pady = (0, 15), padx=(0,20))

    def build_link_popup(self, information, meal_choice):
        information += "\n\nRecipe Link:\n"
        self.details_popup= Toplevel(bg="white")
        self.details_popup.title("Details for " + meal_choice.name.title())
        
        bottom_frame = Frame(self.details_popup, bg="gray95")
        bottom_frame.pack(side=BOTTOM, fill=X)
        ttk.Button(bottom_frame, text="OK", width=12, default="active", command=self.details_popup.destroy).pack(anchor='se', pady = 10, padx = 15)
        
        left_frame = Frame(self.details_popup, width = 40, bg="white")
        left_frame.pack(side=LEFT, fill=Y, padx=(15, 15))
        self.info_icon = Image.open("./information_icon.png")
        self.info_icon = (self.info_icon).resize((50,50))
        self.info_icon = ImageTk.PhotoImage(self.info_icon)
        self.info_icon_label = Label(left_frame, image=self.info_icon, bg="white", padx=10, pady=20)
        self.info_icon_label.pack(anchor='n')

        Label(self.details_popup, text= information, justify = LEFT, bg="white", wraplength=300).pack(anchor = "w", padx=(0, 20), pady=(15,0))
        self.create_hyperlink(meal_choice.link)
        return