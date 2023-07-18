from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500, 700)

Builder.load_file('calculator.kv')


class CalculatorLayout(Widget):
    pass


class CalculatorApp(App):

    math_signs = ['+', '-', 'x', '/']
    equals_pressed = False

    def __init__(self):
        super().__init__()
        self.calculator_frontend = CalculatorLayout()

    def btn_press(self, button):
        current = self.calculator_frontend.ids.calc_window.text
        if current == '0' or self.equals_pressed:
            self.calculator_frontend.ids.calc_window.text = f'{button}'
        else:
            self.calculator_frontend.ids.calc_window.text = f'{current}{button}'
        self.equals_pressed = False

    def dot(self):
        current = self.calculator_frontend.ids.calc_window.text
        nums = current.split('+')

        if self.equals_pressed:
            self.calculator_frontend.ids.calc_window.text = '.'
            self.equals_pressed = False
        else:
            if '.' not in nums[-1]:
                self.calculator_frontend.ids.calc_window.text = f'{current}.'

    def sign_change(self):
        current = self.calculator_frontend.ids.calc_window.text

        if current != '0':
            if current.startswith('-'):
                self.calculator_frontend.ids.calc_window.text = current[1:]
            else:
                self.calculator_frontend.ids.calc_window.text = f'-{current}'

    def math_sign(self, sign):
        if self.calculator_frontend.ids.calc_window.text == "Error: division by zero":
            self.calculator_frontend.ids.calc_window.text = '0'
        else:
            current = self.calculator_frontend.ids.calc_window.text
            if not current.endswith('**'):
                if current[-1] not in self.math_signs:
                    self.calculator_frontend.ids.calc_window.text = f'{current}{sign}'
                if sign == '*' and current[-1] == '*':
                    self.calculator_frontend.ids.calc_window.text = f'{current}{sign}'
            self.equals_pressed = False

    def percent(self):
        pass

    def clear(self):
        self.calculator_frontend.ids.calc_window.text = '0'

    def clear_last(self):
        current = self.calculator_frontend.ids.calc_window.text
        if len(current) > 1:
            self.calculator_frontend.ids.calc_window.text = current[:-1]
        else:
            self.calculator_frontend.ids.calc_window.text = '0'

    def equals(self):
        self.equals_pressed = True
        try:
            answer = str(eval(self.calculator_frontend.ids.calc_window.text))
            if answer.endswith('.0'):
                self.calculator_frontend.ids.calc_window.text = answer[:-2]  # remove the '.0' at the end of the result
            else:
                self.calculator_frontend.ids.calc_window.text = answer
        except ZeroDivisionError:
            self.calculator_frontend.ids.calc_window.text = "Error: division by zero"

    def build(self):
        return self.calculator_frontend


if __name__ == '__main__':
    CalculatorApp().run()