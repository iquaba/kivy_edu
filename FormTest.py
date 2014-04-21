import csv
import random
import sys
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

        self.points = 0
        self.questions = {}
        self.qcount = 0
        self.rightanswer = 0
        self.result = "Wrong!"

        # Load questions from CSV
        with open ('questions.csv') as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            self.qcount = 0
            for row in reader:
                for i in range(0,7):
                    self.questions[self.qcount, i] = row[i]
                self.qcount += 1

        self.popquiz()

        pass

    def popquiz(self):

        questext = ''
        a1 = ''
        a2 = ''
        a3 = ''
        a4 = ''

        i = random.randint(0,self.qcount - 1)

        questext = self.questions[i, 1]
        a1 = self.questions[i, 2]
        a2 = self.questions[i, 3]
        a3 = self.questions[i, 4]
        a4 = self.questions[i, 5]
        self.rightanswer = int(self.questions[i, 6])

        # set up columns
        self.cols = 2

        # set up the question
        self.labelq = Label(text='Q',width=10)
        self.labelqtxt = Label(text=questext,size_hint_x=5)

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
        self.label1 = Label(text=a1,size_hint_x=5)
        self.label2 = Label(text=a2,size_hint_x=5)
        self.label3 = Label(text=a3,size_hint_x=5)
        self.label4 = Label(text=a4,size_hint_x=5)

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



    def on_button_pressed(instance, value):
        # TODO: Pull the student's score from the server
        # TODO: Upload new score to the server
        # TODO: Mark answered questions so they aren't asked again

        # points value would be pulled from server at this point

        # Correct answer is a 4-bit field
        # a = 8, b = 4, c = 2, d = 1
        #  ex.: If a and c are both correct, correct answer is 10

        bitfieldanswer = 0

        if instance.checkbox1.active: bitfieldanswer |= 8
        if instance.checkbox2.active: bitfieldanswer |= 4
        if instance.checkbox3.active: bitfieldanswer |= 2
        if instance.checkbox4.active: bitfieldanswer |= 1

        print(bitfieldanswer)

        if bitfieldanswer == instance.rightanswer:
            instance.points += 10
            instance.result = 'Correct! You now have '+str(instance.points)+' points.'
            print(instance.result)
        else:
            instance.points -= 10
            instance.result = 'Wrong! You now have '+str(instance.points)+' points.'
            print (instance.result)

        print ('You now have ',instance.points, 'points.')

        instance.destroyGUI()
        #instance.popquiz()
        instance.displayResult()

    def displayResult(self):
        self.cols = 1
        self.add_widget(Label(text=self.result))
        btnNewQuestion = Button(text='New Question')
        btnNewQuestion.bind(on_press=self.NewQuestion)
        self.add_widget(btnNewQuestion)

    def NewQuestion(instance,value):
        instance.destroyGUI()
        instance.popquiz()


    def destroyGUI(self):
        # Tear down the interface to a blank GridLayout
        if DEBUG_MODE: print ('killing current GUI')

        self.clear_widgets()

        pass

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