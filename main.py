# importing the required libraries
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
from PyQt5.QtCore import Qt


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowFlag(Qt.FramelessWindowHint)

		self.setWindowOpacity(.15)

		self.setGeometry(950, 20, 370, 200)

		uic.loadUi('main.ui',self)


		# show all the widgets
		self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())
