from tkinter import *

class Calculator:
    def __init__(self, root):
        root.title("Calculator")
        root.geometry("357x420+0+0")
        root.config(bg="gray")
        root.resizable(False, False)

        self.equation = StringVar()
        self.current_expression = ""

        # Entry widget for displaying input/output
        Entry(width=17, bg="lightblue", font=("Arial Bold", 28), textvariable=self.equation).place(x=0, y=0)

        # Button layout
        buttons = [
            ("(", 0, 50), (")", 90, 50), ("%", 180, 50), ("/", 270, 50),
            ("7", 0, 125), ("8", 90, 125), ("9", 180, 125), ("*", 270, 125),
            ("4", 0, 200), ("5", 90, 200), ("6", 180, 200), ("-", 270, 200),
            ("1", 0, 275), ("2", 90, 275), ("3", 180, 275), ("+", 270, 275),
            ("C", 0, 350), ("0", 90, 350), (".", 180, 350), ("=", 270, 350),
        ]

        # Create buttons
        for (text, x, y) in buttons:
            Button(
                width=11, height=4, text=text, relief="flat", bg="white",
                command=lambda t=text: self.on_button_click(t)
            ).place(x=x, y=y)

        #Binding keyboard events to the root window
        root.bind("<Key>", self.key_press)  # Bind all keypress events

    def on_button_click(self, char):
        if char == "C":
            self.clear()
        elif char == "=":
            self.calculate()
        else:
            self.current_expression += str(char)
            self.equation.set(self.current_expression)

    def calculate(self):
        try:
            # Safely evaluate the expression
            result = eval(self.current_expression)
            self.equation.set(result)
            self.current_expression = str(result)
        except ZeroDivisionError:
            self.equation.set("Error: Div by 0")
            self.current_expression = ""
        except Exception:
            self.equation.set("Error")
            self.current_expression = ""

    def clear(self):
        self.current_expression = ""
        self.equation.set("")

    #keypress events
    def key_press(self, event):
        key = event.char  # Get the character of the key pressed
        if key in "0123456789+-*/().%":  #  only valid characters are aalowed
            self.current_expression += key
            self.equation.set(self.current_expression)
        elif key == "\r":  # Enter key to calculate
            self.calculate()
        elif key == "\x08":  # Backspace key to remove last character
            self.current_expression = self.current_expression[:-1]
            self.equation.set(self.current_expression)

root = Tk()
cal = Calculator(root)
root.mainloop()
