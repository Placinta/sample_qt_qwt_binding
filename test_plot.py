from PySide2.QtWidgets import QApplication
import pysideqwt
app = QApplication([])
plot = pysideqwt.QwtPlot()
plot.show()
app.exec_()
del app
