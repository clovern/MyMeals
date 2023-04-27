from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from abc import ABC, abstractmethod

class Page(ABC):
    def __init__(self):
        self.hide_frame = ttk.Frame(self.outer)
        self.hide_frame.grid(column = 0, row = 0)
    
    def create_header_frame(self):
        self.headercontent = ttk.Frame(self.hide_frame, width=800, height = 30)
        self.headercontent.grid_propagate(0)
        self.headercontent.grid(column=0, row=0)

    def create_upper_frame(self):
        self.uppercontent= ttk.Frame(self.hide_frame)
        self.uppercontent.grid(column=0, row=1)
    
    def create_lower_frame(self):
        self.lowercontent = ttk.Frame(self.hide_frame, height=600, width=800)
        self.lowercontent.grid(column=0, row=2, pady = (10, 0))
        self.lowercontent.grid_propagate(0)
    
    def create_lower_left_frame(self):
        self.lower_left_content = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lower_left_content.grid(column=0, row=0)
        self.lower_left_content.grid_propagate(0)
    
    def create_lower_right_frame(self):
        self.lower_right_content = ttk.Frame(self.lowercontent, height=550, width=400)
        self.lower_right_content.grid(column=1, row=0)
        self.lower_right_content.grid_propagate(0) 

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
    
    def create_back_button(self):
        self.back_button = ttk.Button(self.headercontent, default = "active", text = u"\U0001F814", command=self.return_to_last_page)
        self.back_button.grid(column=0, row=0, sticky = NW, padx = (15, 0), pady = (5, 0))
    
    def clear_page(self):
        self.hide_frame.grid_forget()