import sys
from PyQt4 import QtGui, QtCore
import fra
import os



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(350, 250)
        self.setWindowTitle('mainwindow')


        exit = QtGui.QAction(QtGui.QIcon(''), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        
        openAction = QtGui.QAction('Open', self) 
        openAction.setShortcut('Ctrl+O') 
        openAction.setStatusTip('Open a file') 
        openAction.triggered.connect(self.openFile)

        exportAction = QtGui.QAction('Export', self) 
        exportAction.setShortcut('Ctrl+E') 
        exportAction.setStatusTip('Export as P00 file') 
        exportAction.triggered.connect(self.exportFile)
        
        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        file.addAction(openAction)
        file.addAction(exportAction)


    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME')) 
        self.Data = fra.Data()
        self.Data.setData(filename)
        
    def exportFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".P00")
        self.Data.saveP00(filename)

        
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
