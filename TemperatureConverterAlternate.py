'''
Version One
This program will convert Temperatures of Celcius and Farenheit Interchangably
'''
from tkinter import *
CELCIUSABSOLUTEZERO = -273.15
FARENHEITABSOLUTEZERO = -459.67

def run(master):
    # Runs program
    master.mainloop()

# Button Functions
def back(master):
    ''' Closes window and opens home window '''
    master.destroy()
    Main()
def calculate(entry, label, convert_to):
    ''' Calculates and validates entry '''
    try:
        if convert_to=='c':
            if float(entry.get())>=FARENHEITABSOLUTEZERO:
                label.configure(text=str((float(entry.get())-32)/1.8)+'C')
            else:
                label.configure(text='Enter value above absolute zero ('+str(FARENHEITABSOLUTEZERO)+'F)')
        elif convert_to=='f':
            if float(entry.get())>=CELCIUSABSOLUTEZERO:
                label.configure(text=str(float(entry.get())*1.8+32)+'F')
            else:
                label.configure(text='Enter value above absolute zero ('+str(CELCIUSABSOLUTEZERO)+'C)')
    except ValueError:
        label.configure(text='Enter Only Numbers')
def reset(entry, label):
    ''' Resets converted temperature label and clears entry box'''
    entry.delete(0,END)
    label.configure(text='Converted Temperature Goes Here')

class Main:
    def __init__(self):
        self.master=Tk()
        self.master.title('Temperature Converter')

        # Makes Widgets expand as window is resized
        for i in range(2):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(2):
            self.master.grid_columnconfigure(j, weight=1)

        # Title
        self.l_title=Label(self.master, text='Temperature Converter', font='Arial 20 bold')
        self.l_title.grid(columnspan=2, row=0, sticky='nsew')

        # Converter Buttons
        self.b_celcius = Button(self.master, text='to Celcius', font='Arial 15 bold', bg='yellow', command=self.open_c)
        self.b_celcius.grid(row=1, column=0,sticky='nsew')

        self.b_farenheit = Button(self.master, text='to Farenheit', font='Arial 15 bold', bg='red', command=self.open_f)
        self.b_farenheit.grid(row=1, column=1,sticky='nsew')

        run(self.master)

    def open_f(self):
        # Creates new window and closes current
        To_Farenheit()
        self.master.destroy()
    def open_c(self):
        # Creates new window and closes current
        To_Celcius()
        self.master.destroy()

class To_Farenheit:
    def __init__(self):
        self.master=Tk()
        self.master.title('Temperature Converter')
        
        # Makes Widgets expand as window is resized
        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.master.grid_columnconfigure(j, weight=1)

        # Title
        self.l_title=Label(self.master, text='Enter Temperature in Celcius', font='Arial 15 bold')
        self.l_title.grid(columnspan=3, row=0, sticky='nsew')

        # User Entry 
        self.e_celcius= Entry(self.master, justify=CENTER)
        self.e_celcius.grid(row=1, columnspan=3,sticky='ew')

        # Buttons
        self.b_calc = Button(self.master, text='Calculate', font='Arial 10', command=lambda:calculate(self.e_celcius, self.l_ftemperature, 'f'))
        self.b_calc.grid(row=2, column=0,sticky='nsew')

        self.b_back = Button(self.master, text='Back', font='Arial 10', command=lambda:back(self.master))
        self.b_back.grid(row=2, column=1,sticky='nsew')

        self.b_reset = Button(self.master, text='Reset', font='Arial 10', command=lambda:reset(self.e_celcius,self.l_ftemperature))
        self.b_reset.grid(row=2, column=2,sticky='nsew')

        # Calculated Temperature
        self.l_ftemperature=Label(self.master, text='Converted Temperature Goes Here', font='Arial 8')
        self.l_ftemperature.grid(columnspan=3, row=3, sticky='nsew')

class To_Celcius:
    def __init__(self):
        self.master=Tk()
        self.master.title('Temperature Converter')

        for i in range(4):
            self.master.grid_rowconfigure(i, weight=1)
        for j in range(3):
            self.master.grid_columnconfigure(j, weight=1)

        # Title
        self.l_title=Label(self.master, text='Enter Temperature in Farenheit', font='Arial 15 bold')
        self.l_title.grid(columnspan=3, row=0, sticky='nsew')

        # User Entry 
        self.e_farenheit= Entry(self.master, justify=CENTER)
        self.e_farenheit.grid(row=1, columnspan=3,sticky='ew')

        # Buttons
        self.b_calc = Button(self.master, text='Calculate', font='Arial 10', command=lambda:calculate(self.e_farenheit, self.l_ctemperature, 'c'))
        self.b_calc.grid(row=2, column=0,sticky='nsew')

        self.b_back = Button(self.master, text='Back', font='Arial 10', command=lambda:back(self.master))
        self.b_back.grid(row=2, column=1,sticky='nsew')

        self.b_reset = Button(self.master, text='Reset', font='Arial 10', command=lambda:reset(self.e_farenheit,self.l_ctemperature))
        self.b_reset.grid(row=2, column=2,sticky='nsew')

        # Calculated Temperature
        self.l_ctemperature=Label(self.master, text='Converted Temperature Goes Here', font='Arial 8')
        self.l_ctemperature.grid(columnspan=3, row=3, sticky='nsew')

# Creates Main Window
Main()