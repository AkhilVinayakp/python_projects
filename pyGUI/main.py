from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
import sys

app  = QGuiApplication(sys.argv)

# adding the engine to 
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
#  just sending the signal to quit our app when close signal send from the qml engine

# loading the ui 
engine.load("main.qml")



sys.exit(app.exec_())