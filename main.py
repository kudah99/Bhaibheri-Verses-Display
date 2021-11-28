# importing the required libraries
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QMainWindow,QApplication ,QMenu,QSystemTrayIcon
from PyQt5 import uic
from PyQt5.QtCore import Qt
import csv
from random import choice


class CustomDisplay(QDialog):
	def __init__(self):
		super().__init__()

		uic.loadUi('customDisplay.ui', self)

		self.setWindowTitle('Custom Display Settings')

		self.show()

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.currentVerse = None

		self.currentVerseContent = None

		def getRandomVerse():

			with open('data_sho.csv' , encoding='utf8') as f:
				csv_reader = csv.reader(f)

				verse = list(csv_reader)
				random_verse = choice(verse)

				self.currentVerseContent = random_verse[1]
				self.currentVerse = random_verse[0]

			return random_verse[0]+','+random_verse[1]

		getRandomVerse()


	
		self.setWindowFlag(Qt.FramelessWindowHint)

		#self.setWindowOpacity(.09)

		self.setWindowFlag(QtCore.Qt.Tool)

		self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

		self.setGeometry(950, 20, 370, 200)

		uic.loadUi('main.ui',self)

		self.verses_content = self.findChild(QtWidgets.QLabel, 'verse_content')

		self.verses =  self.findChild(QtWidgets.QLabel, 'verse')

		self.verses_content.setText(self.currentVerseContent)

		self.verses.setText(self.currentVerse)

		# show all the widgets
		self.show()



# create pyqt5 app
App = QApplication(sys.argv)

trayIco = QSystemTrayIcon(QIcon('64.png') , parent=App)
trayIco.show()
menu = QMenu()

customize = menu.addAction('Custom display Settings')

aboutUs = menu.addAction('About App')
quitApp = menu.addAction('Exit or close App')
quitApp.triggered.connect(App.quit)
trayIco.setContextMenu(menu)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
