from PyQt5.QtWidgets import QApplication, QWidget
import sys

App = QApplication(sys.argv)

window = QWidget()
window.show()

sys.exit(app.exec_())