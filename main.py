import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from weather import Ui_Dialog
from pyowm import OWM

# create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hook logic
def get_weather_city ():
	owm = OWM ("89a00c8ba17cc892007b41c6058ebb82")
	city = ui.lineEdit.text ()

	# Search for current weather in London (Great Britain)
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather
	temperature = w.temperature ("celsius")
	print(w)
	# <Weather - reference time=2013-12-18 09:20, status=Clouds>

	ui.label.setText (f"Температура:{temperature}")
	print ("Ivan gay")

ui.pushButton.clicked.connect (get_weather_city)

# Main loop
sys.exit(app.exec_())