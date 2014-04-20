from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox

DEBUG_MODE = bool(False)

class FormTestGame(GridLayout):

    def __init__(self,**kwargs):
        super(FormTestGame,self).__init__(**kwargs)

        # set up columns
        self.cols = 2

        # set up the question
        self.labelq = Label(text='Q',width=10)
        self.labelqtxt = Label(text='Here is the text of the question.',size_hint_x=5)

        # set up checkboxes
        self.checkbox1 = CheckBox(width=10)
        self.checkbox2 = CheckBox(width=10)
        self.checkbox3 = CheckBox(width=10)
        self.checkbox4 = CheckBox(width=10)
        self.checkbox1.bind(active=self.on_checkbox_active)
        self.checkbox2.bind(active=self.on_checkbox_active)
        self.checkbox3.bind(active=self.on_checkbox_active)
        self.checkbox4.bind(active=self.on_checkbox_active)

        # set up answers
        self.label1 = Label(text='a) answer uno',size_hint_x=5)
        self.label2 = Label(text='b) answer dos',size_hint_x=5)
        self.label3 = Label(text='c) answer tres',size_hint_x=5)
        self.label4 = Label(text='d) answer cuatro',size_hint_x=5)

        # set up button
        self.btnSubmitAnswer = Button(text='Submit!')
        self.btnSubmitAnswer.bind(on_press=self.on_button_pressed)

        # display question, answers, and submit button
        self.add_widget(self.labelq)
        self.add_widget(self.labelqtxt)
        self.add_widget(self.checkbox1)
        self.add_widget(self.label1)
        self.add_widget(self.checkbox2)
        self.add_widget(self.label2)
        self.add_widget(self.checkbox3)
        self.add_widget(self.label3)
        self.add_widget(self.checkbox4)
        self.add_widget(self.label4)
        self.add_widget(Label())
        self.add_widget(self.btnSubmitAnswer)
        pass


    def on_button_pressed(instance, value):
        # TODO: Pull the student's score from the server
        # TODO: Check for the correct answer
        # TODO: Upload new score to the server

        # points value would be pulled from server at this point
        points = 0

        # Right now this only checks for whether the first checkbox is checked

        if instance.checkbox1.active:
            points += 10
            print('Correct!')
        else:
            points -= 10
            print ('Wrong!')

        print ('You now have ',points, 'points.')


    def on_checkbox_active(self, checkbox, value):
        if DEBUG_MODE:
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')

        pass


class FormTestApp(App):
    def build(self):
        game = FormTestGame()
        return game


if __name__ == '__main__':
    FormTestApp().run()