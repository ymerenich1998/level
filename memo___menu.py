from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont

# вікно для введення запитань
win_menu = QWidget()
win_menu.setWindowTitle('Додавання запитань')\

font = QFont()
font.setPointSize(9)
win_menu.setFont(font)

# віджети для введення запитань
lb_quest = QLabel('Введіть запитання:')
lb_right_ans = QLabel('Введіть вірну відповідь:')
lb_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lb_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lb_wrong_ans3 = QLabel('Введіть третю хибну відповідь')

# віджети для введення тексту
le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

# віджети для відображення статистики
lb_header_stat = QLabel('Статистика')
lb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')

# віджети для відображення статистики
lb_statistic = QLabel()

# віджети для відображення статистики
vl_labels = QVBoxLayout()
vl_labels.addWidget(lb_quest)
vl_labels.addWidget(lb_right_ans)
vl_labels.addWidget(lb_wrong_ans1)
vl_labels.addWidget(lb_wrong_ans2)
vl_labels.addWidget(lb_wrong_ans3)

# віджети для введення тексту
vl_lineEdits = QVBoxLayout()
vl_lineEdits.addWidget(le_question)
vl_lineEdits.addWidget(le_right_ans)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

# віджети для введення тексту
hl_question = QHBoxLayout()
hl_question.addLayout(vl_labels)
hl_question.addLayout(vl_lineEdits)

# віджети для кнопок
btn_Back = QPushButton('Назад')
btn_add_question = QPushButton('Додати запитання')
btn_clear = QPushButton('Очистити')
btn_test = QPushButton('Повна статистика')

# віджети для кнопок
hl_buttons = QHBoxLayout()
hl_buttons.addWidget(btn_add_question)
hl_buttons.addWidget(btn_clear)

# віджети для введення тексту
vl_res = QVBoxLayout()
vl_res.addLayout(hl_question)
vl_res.addLayout(hl_buttons)
vl_res.addWidget(lb_header_stat)
vl_res.addWidget(lb_statistic)
vl_res.addWidget(btn_test)
vl_res.addWidget(btn_Back)

# віджети для введення тексту
win_menu.setLayout(vl_res)
win_menu.resize(550, 450)