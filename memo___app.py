from PyQt5.QtWidgets import QApplication 
from random import shuffle, choice

app = QApplication([])

from time import sleep
from memo___main import *
from memo___menu import *

class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 
        self.actual = True 
        self.count_asked = 0 
        self.count_right = 0 
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_asked += 1

q1 = Question('Яблуко', 'apple', 'application', 'pineapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

question_list = [q1, q2, q3, q4]

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def new_question():
   ''' перемішує питання у картці питання '''
   global cur_q
   cur_q = choice(question_list)
   lb_Question.setText(cur_q.question)
   lb_Correct.setText(cur_q.answer)
   shuffle(radio_list)
   radio_list[0].setText(cur_q.answer)    
   radio_list[1].setText(cur_q.wrong_answer1)
   radio_list[2].setText(cur_q.wrong_answer2)
   radio_list[3].setText(cur_q.wrong_answer3)
    
      
# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
   ''' показати панель відповідей '''
   RadioGroupBox.hide()
   AnsGroupBox.show()
   btn_OK.setText('Наступне питання')

def show_question():
   ''' показати панель питань '''
   RadioGroupBox.show()
   AnsGroupBox.hide()
   btn_OK.setText('Відповісти')
   # скинути вибрану радіо-кнопку
   RadioGroup.setExclusive(False) # зняли обмеження, щоб можна було скинути вибір радіокнопки
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGroup.setExclusive(True) # повернули обмеження, тепер лише одна радіокнопка може бути вибрана

def check_result():
   ''' перевірка, чи правильна відповідь обрана
   якщо відповідь була обрана, то напис "правильно/неправильно" набуває потрібного
   значення і показується панель відповідей
   '''
   for answer in radio_list:
      if answer.isChecked():
         if answer.text() == cur_q.answer:
            lb_Result.setText(text_correct)
            cur_q.got_right()
         else:
            lb_Result.setText(text_wrong)
            cur_q.got_wrong()
         lb_Correct.setText(cur_q.answer)
         show_result()
         return

# Функції для проведення тесту
def click_OK(self):
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if btn_OK.text() != 'Наступне питання':
      check_result()
   else:
      show_question()
      new_question()

def rest():
    win_card.hide()
    sleep(box_Minutes.value() * 60)
    win_card.show()

def click_MENU():
   if cur_q.count_asked  == 0:
      c = 0
   else:
      c = cur_q.count_right / cur_q.count_asked * 100
   text = f"Разів задано: {cur_q.count_asked}\n" \
          f"Правильних відповідей: {cur_q.count_right}\n" \
          f"Відсоток правильних відповідей: {c:.2f}%"
   lb_statistic.setText(text)
   win_menu.show()
   win_card.hide()

def clack_BACK():
    win_menu.hide()
    win_card.show()

show_question()
new_question()

btn_OK.clicked.connect(click_OK)
btn_Sleep.clicked.connect(rest)
btn_Menu.clicked.connect(click_MENU)
btn_Back.clicked.connect(clack_BACK)

win_card.show()
app.exec_()