# importing the required libraries
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt
import csv

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowFlag(Qt.FramelessWindowHint)

		#self.setWindowOpacity(.09)

		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

		self.setGeometry(950, 20, 370, 200)

		self.setStyle

		uic.loadUi('main.ui',self)

		self.verses_content = self.findChild(QtWidgets.QLabel, 'verse_content')

		self.verses =  self.findChild(QtWidgets.QLabel, 'verse')

		self.verses_content.setText('Vakaropafadzwa vakachena pamoyo nokuti vachaona Mwari.')

		self.verses.setText('- Mateo 5:8')

		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
