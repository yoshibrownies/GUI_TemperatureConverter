'''
Version One
This program will convert Temperatures of Celcius and Farenheit Interchangably
'''
from tkinter import *
class Converter:
    # Initating Title Screen
    def __init__(self):
        self.master=Tk()
        self.master.resizable(0,0)
        self.master.title('Temperature Converter')

        # Container for frames
        self.container=Frame(self.master)

        self.frames={}
        self.frames['main_frame']=self.create_main_frame()
        self.show_frame(self.frames['main_frame'])

        


    def run(self):
        # Run program
        self.master.mainloop()
    def show_frame(self, name):
        # Display window
        frame = self.frames[name] # Gets frame
        frame.tkraise() # Brings frame to top
    def create_main_frame(self):
        frame=Frame(self.container)

        self.l_title=Label(frame, text='Temperature Converter', font='Arial 20 bold')
        self.l_title.pack(fill=X)

        # Bottom Frame and Converter Buttons
        
        self.b_celcius = Button(frame, text='to Celcius', font='Arial 15 bold', bg='yellow')
        self.b_celcius.pack(side=LEFT)

        self.b_farenheit = Button(frame, text='to Farenheit', font='Arial 15 bold', bg='red')
        self.b_farenheit.pack(side=LEFT)

        return frame



app=Converter()
app.run()