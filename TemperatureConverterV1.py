'''
Version One
This program will convert Temperatures of Celcius and Farenheit Interchangably
'''
from tkinter import *
CELCIUSABSOLUTEZERO = -273.15
FARENHEITABSOLUTEZERO = -459.67
class Converter:
    # Initating Title Screen
    def __init__(self):
        self.master=Tk()
        self.master.resizable(0,0)
        self.master.title('Temperature Converter')

        # Container for frames
        self.container=Frame(self.master)
        self.container.pack()

        # Dictionary holding all frames
        self.frames={}
        self.frames['main_frame']=self.create_main_frame()
        self.frames['to_f']=self.create_to_f()
        self.frames['to_c']=self.create_to_c()

        # Showing Menu Frame
        self.show_frame('main_frame')

    def run(self):
        # Run program
        self.master.mainloop()

    def show_frame(self, name):
        # Display window
        frame = self.frames[name]# Gets frame
        frame.tkraise() # Brings frame to top

    def create_main_frame(self):
        frame=Frame(self.container)
        frame.grid(row=0, column=0, sticky='nswe')

        # Title
        self.l_title=Label(frame, text='Temperature Converter', font='Arial 20 bold')
        self.l_title.grid(columnspan=2, row=0, sticky='nsew')

        # Converter Buttons
        self.b_celcius = Button(frame, text='to Celcius', font='Arial 15 bold', bg='yellow', command=lambda:self.show_frame('to_c'))
        self.b_celcius.grid(row=1, column=0,sticky='nsew')

        self.b_farenheit = Button(frame, text='to Farenheit', font='Arial 15 bold', bg='red', command=lambda:self.show_frame('to_f'))
        self.b_farenheit.grid(row=1, column=1,sticky='nsew')

        return frame
    
    def create_to_f(self):
        frame=Frame(self.container)
        frame.grid(row=0, column=0, sticky='nswe')

        # Title
        self.l_title=Label(frame, text='Enter Temperature in Celcius', font='Arial 15 bold')
        self.l_title.grid(columnspan=3, row=0, sticky='nsew')

        # User Entry 
        self.e_celcius= Entry(frame, justify=CENTER)
        self.e_celcius.grid(row=1, columnspan=3,sticky='ew')

        # Buttons
        self.b_calc = Button(frame, text='Calculate', font='Arial 10', command=lambda:self.calculate_to('f'))
        self.b_calc.grid(row=2, column=0,sticky='nsew')

        self.b_back = Button(frame, text='Back', font='Arial 10', command=lambda:self.show_frame('main_frame'))
        self.b_back.grid(row=2, column=1,sticky='nsew')

        self.b_reset = Button(frame, text='Reset', font='Arial 10', command=lambda:self.e_celcius.delete(0,END))
        self.b_reset.grid(row=2, column=2,sticky='nsew')

        # Calculated Temperature
        self.l_ftemperature=Label(frame, text='Converted Temperature Goes Here', font='Arial 8')
        self.l_ftemperature.grid(columnspan=3, row=3, sticky='nsew')

        return frame
    
    def create_to_c(self):
        frame=Frame(self.container)
        frame.grid(row=0, column=0, sticky='nswe')

        # Title
        self.l_title=Label(frame, text='Enter Temperature in Farenheit', font='Arial 15 bold')
        self.l_title.grid(columnspan=3, row=0, sticky='nsew')

        # User Entry 
        self.e_farenheit= Entry(frame, justify=CENTER)
        self.e_farenheit.grid(row=1, columnspan=3,sticky='ew')

        # Buttons
        self.b_calc = Button(frame, text='Calculate', font='Arial 10', command=lambda:self.calculate_to('c'))
        self.b_calc.grid(row=2, column=0,sticky='nsew')

        self.b_back = Button(frame, text='Back', font='Arial 10', command=lambda:self.show_frame('main_frame'))
        self.b_back.grid(row=2, column=1,sticky='nsew')

        self.b_reset = Button(frame, text='Reset', font='Arial 10', command=lambda:self.e_farenheit.delete(0,END))
        self.b_reset.grid(row=2, column=2,sticky='nsew')

        # Calculated Temperature
        self.l_ctemperature=Label(frame, text='Converted Temperature Goes Here', font='Arial 8')
        self.l_ctemperature.grid(columnspan=3, row=3, sticky='nsew')

        return frame

    def calculate_to(self, temperature_type):
        # Converts Temperature
        try:
            if temperature_type=='f':
                if float(self.e_celcius.get())>=CELCIUSABSOLUTEZERO:
                    self.l_ftemperature.configure(text=str(float(self.e_celcius.get())*1.8+32)+'F')
                else:
                    self.l_ftemperature.configure(text='Enter value above absolute zero ('+str(CELCIUSABSOLUTEZERO)+'C)')
            elif temperature_type=='c':
                if float(self.e_farenheit.get())>=FARENHEITABSOLUTEZERO:
                    self.l_ctemperature.configure(text=str((float(self.e_farenheit.get())-32)/1.8)+'C')
                else:
                    self.l_ctemperature.configure(text='Enter value above absolute zero ('+str(FARENHEITABSOLUTEZERO)+'F)')

        except ValueError:
            self.l_ftemperature.configure(text='Enter Only Numbers')
            self.l_ctemperature.configure(text='Enter Only Numbers')

app=Converter()
app.run()