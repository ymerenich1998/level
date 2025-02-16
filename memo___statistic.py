#T  test
from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton, QLabel

win_test = QWidget()

win_test.setWindowTitle('Повна статистика')
Tlb_header_stat = QLabel('Статистика')
Tlb_header_stat.setStyleSheet('font-size: 19px; font-weight: bold;')
Tlb_statistic = QLabel()
Tbtn_Back = QPushButton('Назад')

vl_res = QVBoxLayout()
vl_res.addWidget(Tlb_header_stat)
vl_res.addWidget(Tlb_statistic)
vl_res.addWidget(Tbtn_Back)

win_test.setLayout(vl_res)
