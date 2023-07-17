from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


Window.size = (500, 700)

Builder.load_file('calculator.kv')


class NormalLayout(Widget):
    pass


class CalculatorApp(App):
    pass


if __name__ == '__main__':
    CalculatorApp().run()