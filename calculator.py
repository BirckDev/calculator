from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500, 700)

Builder.load_file('calculator.kv')


class CalculatorLayout(Widget):

    def btn_press(self, button):
        prior = self.ids.calc_window.text
        if prior == '0':
            self.ids.calc_window.text = f'{button}'
        else:
            self.ids.calc_window.text = f'{prior}{button}'

    def math_sign(self, sign):
        prior = self.ids.calc_window.text
        self.ids.calc_window.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_window.text
        if '+' in prior:
            num_list = prior.split('+')
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)
            self.ids.calc_window.text = f'{answer}'

    def dot(self):
        if self.ids.calc_window.text[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            self.ids.calc_window.text = f'{self.ids.calc_window.text}.'

    def sign_chang(self):
        if self.ids.calc_window.text == '0':
            pass
        else:
            if self.ids.calc_window.text.startswith('-'):
                self.ids.calc_window.text = self.ids.calc_window.text[1:]
            else:
                self.ids.calc_window.text = f'-{self.ids.calc_window.text}'


class CalculatorApp(App):

    def __init__(self):
        super().__init__()
        self.calculator_frontend = CalculatorLayout()

    def clear(self):
        self.calculator_frontend.ids.calc_window.text = '0'

    def clear_last(self):
        if len(self.calculator_frontend.ids.calc_window.text) > 1:
            self.calculator_frontend.ids.calc_window.text = self.calculator_frontend.ids.calc_window.text[:-1]
        else:
            self.calculator_frontend.ids.calc_window.text = '0'

    def build(self):
        return self.calculator_frontend


if __name__ == '__main__':
    CalculatorApp().run()