from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500, 700)

Builder.load_file('calculator.kv')


class CalculatorLayout(Widget):
    pass


class CalculatorApp(App):

    def __init__(self):
        super().__init__()
        self.calculator_frontend = CalculatorLayout()

    def btn_press(self, button):
        current = self.calculator_frontend.ids.calc_window.text
        if current == '0':
            self.calculator_frontend.ids.calc_window.text = f'{button}'
        else:
            self.calculator_frontend.ids.calc_window.text = f'{current}{button}'

    def dot(self):
        current = self.calculator_frontend.ids.calc_window.text
        nums = current.split('+')

        if '.' not in nums[-1]:
            self.calculator_frontend.ids.calc_window.text = f'{current}.'

    def sign_chang(self):
        current = self.calculator_frontend.ids.calc_window.text

        if current != '0':
            if current.startswith('-'):
                self.calculator_frontend.ids.calc_window.text = current[1:]
            else:
                self.calculator_frontend.ids.calc_window.text = f'-{current}'

    def math_sign(self, sign):
        current = self.calculator_frontend.ids.calc_window.text
        self.calculator_frontend.ids.calc_window.text = f'{current}{sign}'

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
        current = self.calculator_frontend.ids.calc_window.text
        if '+' in current:
            nums = current.split('+')
            answer = 0.0
            for number in nums:
                answer = answer + float(number)
            self.calculator_frontend.ids.calc_window.text = f'{answer}'

    def build(self):
        return self.calculator_frontend


if __name__ == '__main__':
    CalculatorApp().run()