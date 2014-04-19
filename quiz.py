import csv
import random
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

class Quiz():
    def __init__(self):
        self.questions = []
        self.total_correct = 0

    def get_questions(self):
        # This should be some kind of import csv thing
        q1 = Question()
        q1.prompt = "What is 42?"
        q1.choices = ['*42', '30', '21', '81']
        self.append_question(q1)
        
        q2 = Question()
        q2.prompt = "What is 4? (Select all that apply)"
        q2.choices = ['*4', '*four', '31', '59']
        self.append_question(q2)
        
    def append_question(self, question):
        self.questions.append(question)

    def print_question_num(self, num, randomize=False, hint=False):
        '''  Given a question number, print that question
         Starts counting questions at 1 (so num = 1 displays question[0])
         if hint = True, then display answer '''
        
        msg, ans = self.questions[num-1].get_question()
        if hint:
            msg += '\nanswer: ' + ans
        print('Question ' + str(num) + ': ' + msg + '\n')

    def print_entire_quiz(self, randomize=False, hint=False):
        '''  Displays the entire formated quiz.
                randomize=True will shuffle choices
                hint=True will display answer'''
        
        logging.info('Printing quiz: shuffle: {rand}, show answer: {hint}'.format(rand=randomize, hint=hint))
        i = 1;
        for question in self.questions:
            prompt, ans = question.get_question(randomize)
            if(hint):
                prompt += '\nanswer: ' + ans
            if(i != len(self.questions)):       # if this is not the last question
                print('Question ' + str(i) + ': ' + prompt + '\n')
            else:
                print('Question ' + str(i) + ': ' + prompt)
            i+=1
                        
    def check_selection(self, selection, ans):
        ''' Compares user's selection to the correct answer
            returns True if correct and False if incorrect '''
        if ''.join(sorted(selection)) == ans:
            self.total_correct += 1
            return True
        return False

    def get_selection(self):
        return raw_input("Choice(s)? ").upper()

    def grade_quiz(self):
        return float(self.total_correct) / len(self.questions) * 100

    def run_quiz(self, randomize=False):
        question_num = 1
        for question in self.questions:
            prompt, ans = question.get_question(randomize)
            print('Question ' + str(question_num) + ':\n' + prompt)
            question_num += 1
            selection = self.get_selection() 
            result = self.check_selection(selection, ans)
            logging.info('  Correct: ' + str(result) + ', Score: ' + str(self.total_correct) + '\n')
        print('Score: ' + str(self.grade_quiz()) + "%")


class Question():
    def __init__(self):
        self.prompt = ''
        self.choices = []
        self.answer = ''

    def __repr__(self):
        ''' Used with print(). Returns formated string of question & answer '''
        msg, ans = self.get_question()
        msg += '\nanswer: ' + ans
        return(msg)
    
    def __get_choices(self, rand=False):
        ''' Returns a formated string of choices that can be randomized
            along with a sorted string representing the correct answers (eg 'AC'). 
            Requires that the correct choices start with a '*' '''
        ltr = 'A'
        msg = ''
        ans = ''

        choices = self.choices
        if(rand == True):
            random.shuffle(choices)
        
        for choice in choices:
            if choice[0] == '*':    # starting with '*' designates correct answer
                ans += ltr          # save this choice as a correct answer
                choice = choice[1:] # remove '*'
            msg += ltr + ') ' + str(choice) + '\n'
            ltr = chr( ord(ltr) + 1)
      
        msg = msg[:-1]  # remove last new line

        assert(ans==''.join(sorted(ans))) # the answer list must be alphabetical
        return msg, ans

    def get_question(self, rand=False):
        question_string = self.prompt + '\n'
        choices, ans = self.__get_choices(rand)
        question_string += choices
        return question_string, ans

if __name__ == '__main__':
    shuffle = True
    hint = True
    quiz1 = Quiz()
    quiz1.get_questions()
    print('Printing quiz:\n==================================================================')
    quiz1.print_entire_quiz(shuffle, hint)
    print('==================================================================')
    quiz1.run_quiz(shuffle)

