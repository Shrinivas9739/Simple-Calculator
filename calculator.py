from tkinter import *

class Calculator:
    def __init__(self, root):
        root.title("Calculator")
        root.geometry("357x420+0+0")
        root.config(bg="gray")
        root.resizable(False, False)

        self.equation = StringVar()
        self.current_expression = ""
        Entry(width=17, bg="lightblue", font=("Arial Bold", 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            ("(", 0, 50), (")", 90, 50), ("%", 180, 50), ("/", 270, 50),
            ("7", 0, 125), ("8", 90, 125), ("9", 180, 125), ("*", 270, 125),
            ("4", 0, 200), ("5", 90, 200), ("6", 180, 200), ("-", 270, 200),
            ("1", 0, 275), ("2", 90, 275), ("3", 180, 275), ("+", 270, 275),
            ("C", 0, 350), ("0", 90, 350), (".", 180, 350), ("=", 270, 350),
        ]

        for (text, x, y) in buttons:
            Button(
                width=11, height=4, text=text, relief="flat", bg="white",
                command=lambda t=text: self.on_button_click(t)
            ).place(x=x, y=y)

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
            result = eval(self.current_expression)
            self.equation.set(result)
            self.current_expression = str(result)
        except ZeroDivisionError:
            self.equation.set("Error: Div by 0")
            self.current_expression = ""
        except Exception as e:
            self.equation.set("Error")
            self.current_expression = ""

    def clear(self):
        self.current_expression = ""
        self.equation.set("")

root = Tk()
cal = Calculator(root)
root.mainloop()
