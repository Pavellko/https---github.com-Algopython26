from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys

class App(QWidget):
	rezult = "0"
	operator = ""
	def __init__(self):
		super(App, self).__init__()
		self.start()

		self.ui.b0.clicked.connect(self.zero)
		self.ui.b1.clicked.connect(self.one)
		self.ui.b2.clicked.connect(self.two)
		self.ui.b3.clicked.connect(self.three)
		self.ui.b4.clicked.connect(self.four)
		self.ui.b5.clicked.connect(self.five)
		self.ui.b6.clicked.connect(self.six)
		self.ui.b7.clicked.connect(self.seven)
		self.ui.b8.clicked.connect(self.eight)
		self.ui.b9.clicked.connect(self.nine)
		self.ui.back.clicked.connect(self.back_prsd)
		self.ui.clear.clicked.connect(self.clear_prsd)
		self.ui.ravno.clicked.connect(self.ravno_prsd)
		self.ui.delen.clicked.connect(self.delen_prsd)
		self.ui.minus.clicked.connect(self.minus_prsd)
		self.ui.umnoz.clicked.connect(self.umnoz_prsd)
		self.ui.plus.clicked.connect(self.plus_prsd)
		self.ui.zpt.clicked.connect(self.zpt_prsd)
		# self.ui.protsent.clicked.connect(protsent_prsd)

	def start(self):
		self.ui = uic.loadUi("calcus.ui")
		self.ui.show()

	def zero(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}0")
		else:
			self.ui.tablo.setText("0")

	def one(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}1")
		else:
			self.ui.tablo.setText("1")

	def two(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}2")
		else:
			self.ui.tablo.setText("2")
	def three(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}3")
		else:
			self.ui.tablo.setText("3")

	def four(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}4")
		else:
			self.ui.tablo.setText("4")

	def five(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}5")
		else:
			self.ui.tablo.setText("5")

	def six(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}6")
		else:
			self.ui.tablo.setText("6")

	def seven(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}7")
		else:
			self.ui.tablo.setText("7")

	def eight(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}8")
		else:
			self.ui.tablo.setText("8")

	def nine(self):
		val = self.ui.tablo.text()
		if val != "0":
			self.ui.tablo.setText(f"{val}9")
		else:
			self.ui.tablo.setText("9")

	def zpt_prsd(self):
		val = self.ui.tablo.text()
		if not ("." in val):
			self.ui.tablo.setText(f"{val}.")
		else:
			self.ui.tablo.setText(self.ui.tablo.text())

	def back_prsd(self):
		self.ui.tablo.setText(self.ui.tablo.text()[: -1])

	def clear_prsd(self):
		self.ui.tablo.setText("0")

	def plus_prsd(self):
		self.operator = "+"
		self.rezult = self.ui.tablo.text()
		self.ui.tablo.setText("0")

	def minus_prsd(self):
		self.operator = "-"
		self.rezult = self.ui.tablo.text()
		self.ui.tablo.setText("0")

	def delen_prsd(self):
		self.operator = "/"
		self.rezult = self.ui.tablo.text()
		self.ui.tablo.setText("0")

	def umnoz_prsd(self):
		self.operator = "*"
		self.rezult = self.ui.tablo.text()
		self.ui.tablo.setText("0")

	def ravno_prsd(self):
		if not (self.rezult == "0" or self.operator == ""):
			v1 = float(self.rezult)
			v2 = float(self.ui.tablo.text())
			rezult = 0

			if self.operator == "+":
				rezult = v1+v2
			if self.operator == "*":
				rezult = v1*v2

			if self.operator == "/":
				rezult = v1/v2

			if self.operator == "-":
				rezult = v1-v2

			self.rezult = "0"
			self.ui.tablo.setText(str(rezult))


if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()


