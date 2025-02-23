#T  test
from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont

win_test = QWidget()

font = QFont()
font.setPointSize(9)
win_test.setFont(font)

# віджети для відображення статистики
win_test.setWindowTitle('Повна статистика')
Tlb_header_stat = QLabel('Статистика')
Tlb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')
Tlb_statistic = QLabel()
Tbtn_Back = QPushButton('Назад')

# віджети для відображення статистики
vl_res = QVBoxLayout()
vl_res.addWidget(Tlb_header_stat)
vl_res.addWidget(Tlb_statistic)
vl_res.addWidget(Tbtn_Back)

# віджети для відображення статистики
win_test.setLayout(vl_res)
