from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from abc import ABC, abstractmethod

class Page(ABC):
    def __init__(self, root):
        root.title("MyMeals")

    def create_upper_frame(self):
        self.uppercontent= ttk.Frame(self.outer)
        self.uppercontent.grid(column=0, row=0)
    
    def create_lower_frame(self):
        self.lowercontent = ttk.Frame(self.outer, height=600, width=800)
        self.lowercontent.grid(column=0, row=1)
        self.lowercontent.grid_propagate(0)
    
    def create_lower_left_frame(self):
        self.lower_left_content = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lower_left_content.grid(column=0, row=0)
        self.lower_left_content.grid_propagate(0)
    
    def create_lower_right_frame(self):
        self.lower_right_content = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lower_right_content.grid(column=1, row=0)
        self.lower_right_content.grid_propagate(0) 

    # FIXME implement
    def create_nav_bar(self):
        pass

    def create_title(self, title_text):

        self.logo_image = Image.open("./my_meals_logo.png")
        self.logo_image = (self.logo_image).resize((150,150))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_image_label = ttk.Label(self.uppercontent, image=self.logo_image)
        # below line resolves tkinter bug with saving image files
        self.logo_image_label.image = self.logo_image
        self.logo_image_label.grid(column=0, row=0)


        self.title = ttk.Label(self.uppercontent, text=title_text, font=("Arial", 25))
        self.title['padding'] = (40, 40, 40, 40)
        self.title.grid(column=1, row=0)
    
    def clear_page(self):
        self.uppercontent.destroy()
        self.lowercontent.destroy()