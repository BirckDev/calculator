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
        prior = self.calculator_frontend.ids.calc_window.text
        if prior == '0':
            self.calculator_frontend.ids.calc_window.text = f'{button}'
        else:
            self.calculator_frontend.ids.calc_window.text = f'{prior}{button}'

    def dot(self):
        prior = self.calculator_frontend.ids.calc_window.text
        nums = prior.split('+')

        if '.' not in nums[-1]:
            self.calculator_frontend.ids.calc_window.text = f'{prior}.'

    def sign_chang(self):
        if self.calculator_frontend.ids.calc_window.text == '0':
            pass
        else:
            if self.calculator_frontend.ids.calc_window.text.startswith('-'):
                self.calculator_frontend.ids.calc_window.text = self.calculator_frontend.ids.calc_window.text[1:]
            else:
                self.calculator_frontend.ids.calc_window.text = f'-{self.calculator_frontend.ids.calc_window.text}'

    def math_sign(self, sign):
        prior = self.calculator_frontend.ids.calc_window.text
        self.calculator_frontend.ids.calc_window.text = f'{prior}{sign}'

    def percent(self):
        pass

    def clear(self):
        self.calculator_frontend.ids.calc_window.text = '0'

    def clear_last(self):
        if len(self.calculator_frontend.ids.calc_window.text) > 1:
            self.calculator_frontend.ids.calc_window.text = self.calculator_frontend.ids.calc_window.text[:-1]
        else:
            self.calculator_frontend.ids.calc_window.text = '0'

    def equals(self):
        prior = self.calculator_frontend.ids.calc_window.text
        if '+' in prior:
            num_list = prior.split('+')
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)
            self.calculator_frontend.ids.calc_window.text = f'{answer}'

    def build(self):
        return self.calculator_frontend


if __name__ == '__main__':
    CalculatorApp().run()