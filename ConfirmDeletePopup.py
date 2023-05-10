from tkinter import *
from tkinter import ttk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk

class ConfirmDeletePopup:

    def __init__(self, meal, recipe_book):
        self.meal = meal
        self.build_confirmdelete_popup()
        self.recipe_book = recipe_book

    def build_confirmdelete_popup(self):
        self.found_frame = None
        self.delete_popup= Toplevel(bg="white")
        self.delete_popup.title("Confirm Meal Delete")

        bottom_frame = Frame(self.delete_popup, bg="gray95")
        bottom_frame.pack(side=BOTTOM, fill=X)
        ttk.Button(bottom_frame, text="DELETE", width=12, default="active", command=self.confirm_delete).pack(anchor='se', pady = (10, 3), padx = 15)
        ttk.Button(bottom_frame, text="KEEP", width=12, default="active", command = self.delete_popup.destroy).pack(anchor='se', pady = (3, 10), padx = 15)

        left_frame = Frame(self.delete_popup, width = 40, bg="white")
        left_frame.pack(side=LEFT, fill=Y, padx=(15, 15))
        self.info_icon = Image.open("./delete_icon.png")
        self.info_icon = (self.info_icon).resize((50,50))
        self.info_icon = ImageTk.PhotoImage(self.info_icon)
        self.info_icon_label = Label(left_frame, image=self.info_icon, bg="white")
        self.info_icon_label.pack(anchor='n', padx=0, pady=20)

        text = "\n\nAre you sure you want to delete " + self.meal.name + " from your saved recipes?\n"
        Label(self.delete_popup, text= text, justify = LEFT, bg="white", wraplength=300).pack(anchor = "n", padx=(10, 40), pady=(0,0))
        
        return
    
    def confirm_delete(self):
        self.recipe_book.remove_meal(self.meal)
        self.delete_popup.destroy()