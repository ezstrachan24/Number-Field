"""
program: numberfielddemo.py
author: edwardstrachan
"""

from breezypythongui import EasyFrame
import math

class NumberFieldDemo(EasyFrame):
    """Computes and displays teh sqaure root of an input number."""
    
    def __init__(self):
        """Sets up the winow ans widgets."""
        EasyFrame.__init__(self, title = "Number Field Demo")

        # Create the nested frame for data panel
        dataPanel = self.addPanel(row = 0, column=0, background="blue")
        
        # Label and field for the input
        self.addLabel(text = "An Integer", row = 0, column = 0, background="green")
        self.inputField = self.addIntegerField(value = 0, row = 0, column = 1, width = 10)

        # Label and field for the output
        self.addLabel(text = "Square Root", row = 1, column = 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, state = "readonly")

        # The command button
        self.addButton(text = "Submit", row = 2, column = 0, columnspan = 2, command = self.submitSqrt)

    # The event handling method for the button
    def submitSqrt(self):
        """Inputs the integer, Computes the square root, and outputs result. Handles input errors by displaying a mesage box"""
        try:
            number = self.inputField.getNumber()
            result = math.sqrt(number)
            self.outputField.setNumber(result)
        except ValueError:
            self.messageBox(title = "ERROR", message= "Input must be a Number SmartyPants -__-")

def main():
    NumberFieldDemo().mainloop()
main()