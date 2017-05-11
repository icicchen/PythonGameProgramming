import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QDockWidget,  QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraphdev.pyqtgraph as pt
from pyqtgraphdev.pyqtgraph import PlotWidget
import numpy as np
import time


class HistGraph(QDockWidget):
    def __init__(self, parent = None):
        super(HistGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # -- container for histogram (same as graph)
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("hostHist")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(500, 200)
        # -- define the histogram
        self.graph = PlotWidget(self)
        # -- horizontal, vertical lines, and thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("hsplot")
        self.graph.raise_()
        # -- add graph container to layout
        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, data):
        Y = data['Y']
        # -- using Numpy to calculate the histogram
        y , x = np.histogram(Y)
        lineColor = data['pen']
        self.graph.clear()
        self.graph.plot(x, y, stepMode = True, fillLevel = 0, brush = (0,0,255,255))

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9 * e.size().height())

class MainGraph(QDockWidget):
    def __init__(self, parent = None):
        super(MainGraph, self).__init__(parent=parent)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        # -- container for graph
        self.host = QtWidgets.QWidget(self)
        self.host.setObjectName("hostGraph")
        self.host.setSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        self.host.setMinimumSize(500, 200)
        # -- define the graph
        self.graph = PlotWidget(self)
        # -- horizontal, vertical lines, and thickness
        self.graph.plotItem.showGrid(True, True, 0.7)
        self.setObjectName("grplot")
        self.graph.raise_()
        # -- add graph container to layout
        self.verticalLayout = QVBoxLayout(self.host)
        self.verticalLayout.addWidget(self.graph)

    def plot(self, data):
        '''
        :param data: dictionary with X, Y data
        :return: None
        '''
        X = data['X']
        Y = data['Y']
        colorLine = data['pen']
        self.graph.plot(X, Y, pen=colorLine, clear=True)

    def resizeEvent(self, e):
        self.host.setGeometry(10, 10, e.size().width(), e.size().height())
        self.graph.setGeometry(10, 10, e.size().width(), 0.9 * e.size().height())


class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(Mainwindow, self).__init__(parent=parent)
        self.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AnimatedDocks)
        # -- create docks
        self.dockGraph = MainGraph()
        self.dockHist = HistGraph()
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dockGraph)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dockHist)
        self.update()

    def update(self):
        Npoints = 500
        X = np.arange(Npoints)
        Y = np.random.poisson(5.0, Npoints)
        # -- every second we change color with this command
        C = pt.hsvColor(time.time() / 5 % 1, alpha = 0.5)
        # -- Pyqtgraph wrapper for the line.
        pen = pt.mkPen(color = C, width = 2)
        data = {'X':X, 'Y':Y, 'pen':pen}
        self.dockGraph.plot(data)
        self.dockHist.plot(data)
        # -- refresh rate of 100 ms
        QtCore.QTimer.singleShot(100, self.update)


class SandBoxApp(QtWidgets.QApplication):
    # -- define class constructor
    def __init__(self, *args, **kwargs):
        super(SandBoxApp, self).__init__(*args)
        self.mainwindow = Mainwindow()
        self.mainwindow.setGeometry(50, 100, 1200, 600)
        self.mainwindow.show()
        # -- disable contextual menu (right click mouse)
        self.mainwindow.setContextMenuPolicy(Qt.NoContextMenu)

# -- entry point for the Python program
def main():
    app = SandBoxApp(sys.argv)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

