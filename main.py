from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class CalculatorLayout(GridLayout):

    icon = StringProperty("del.png")

    def calculate(self, calculation_val):
        if calculation_val:
            try:
                self.display.text = str(eval(calculation_val))
            except Exception:
                self.display.text = "Error"

    def validate(self, val, input):
        if val:
            if val[-1] not in ('+', '-', '*', '/', '.'):
                self.display.text = str(val) + input


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

if __name__ == '__main__':
    CalculatorApp().run()