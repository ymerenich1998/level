from PyQt5.QtWidgets import QApplication 

app = QApplication([])

from memo___main import *

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
   correct = answer.isChecked() # у цьому радіобаттоні лежить наша відповідь!
   if correct:
       # відповідь вірна, запишемо
       lb_Result.setText(text_correct) # напис "правильно" або "неправильно"
       show_result()
   else:
       incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
       if incorrect:
           # відповідь невірна, запишемо і відобразимо у статистиці
           lb_Result.setText(text_wrong) # напис "правильно" або "неправильно"
           show_result()

def click_OK(self):
   # поки що перевіряємо питання, якщо ми в режимі питання, інакше нічого
   if btn_OK.text() != 'Наступне питання':
      check_result()
   else:
      show_question()
      show_data()
    

show_question()
show_data()

btn_OK.clicked.connect(click_OK)

app.exec_()