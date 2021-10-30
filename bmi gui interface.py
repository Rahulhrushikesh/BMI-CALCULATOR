
# Imports all from Tkinter GUI Package
from tkinter import *

# Initialization
box = Tk()
weight = IntVar(None)
height = IntVar(None)
result = IntVar(None)


# Calculates Body Mass Index (BMI) with user inputs, then put the user in one of four categories
# Also check if the values entered are not zero

def calculator_bmi():
    try:
        bmi = float(mass.get()) / (float(height.get()) * float(height.get()))
        result.set(bmi)
    except ZeroDivisionError:
        weight.set(None)
        height.set(None)
        result.set(None)
        return
    if bmi < 18.5:
        resLabelText.set("you are categorised as Underweight")
    if 18.5 < bmi < 24.9:
        resLabelText.set("you are categorised as Normal")
    if 25 < bmi < 29.9:
        resLabelText.set("you are categorised as Overweight")
    if bmi > 30:
        resLabelText.set("you are categorised as Obese")
    return

# Graphical User Interface (Tkinter) 

#  Sets size and title 
box.geometry("450x250+150+150")
box.title("BMI Calculator")

# Label and test box for mass in kg
mLabelText = StringVar()
mLabelText.set("Enter your weight in kg: ")
massLabel = Label(box, textvariable=mLabelText)
massLabel.pack()

mass = Entry(box, textvariable=weight)
mass.pack()

# Label and text box for height
hLabelText = StringVar()
hLabelText.set("Enter your height in meter: ")
heightLabel = Label(box, textvariable=hLabelText)
heightLabel.pack()

height = Entry(box, textvariable=height)
height.pack()

# Button and label and textbox for BMI calculation
button = Button(box, text="Calculate BMI", command=calculator_bmi)
button.pack(padx=20, pady=20)
bmiLabelText = StringVar()
bmiLabelText.set("Your BMI is: ")
bmiLabel = Label(box, textvariable=bmiLabelText)
bmiLabel.pack()

bmi = Entry(box, textvariable=result)
bmi.pack()
resLabelText = StringVar()
resLabelText.set(" you are categorised as: ")
resLabel = Label(box, textvariable=resLabelText)
resLabel.pack()

# Starts the GUI 
box.mainloop()
