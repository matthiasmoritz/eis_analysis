import sys
from PyQt4 import QtGui, QtCore
import fra
import os
import proj



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(250, 150)
        self.setWindowTitle('EIS')
        
        #input
        self.pp = QtGui.QLineEdit(self)
        self.pp.setGeometry(10, 30, 200, 20)
        self.pp.setEnabled(False)

        self.out = QtGui.QLineEdit(self)
        self.out.setGeometry(10, 60, 200, 20)
        self.out.setEnabled(False)

        exit = QtGui.QAction(QtGui.QIcon(''), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        
        openAction = QtGui.QAction('Open File', self) 
        openAction.setShortcut('Ctrl+O') 
        openAction.setStatusTip('Open a file') 
        openAction.triggered.connect(self.openFile)

        openDirAction = QtGui.QAction('Open Directory', self) 
        openDirAction.setStatusTip('Open a directory') 
        openDirAction.triggered.connect(self.openDir)

        exportAction = QtGui.QAction('Export', self) 
        exportAction.setShortcut('Ctrl+E') 
        exportAction.setStatusTip('Export as P00 file') 
        exportAction.triggered.connect(self.exportFile)
        
        self.statusBar()
        
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        file.addAction(openAction)
        file.addAction(openDirAction)
        file.addAction(exportAction)


    def openFile(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        self.Data = fra.Data()
        self.Data.setData(filename)
        self.pp.setText(filename)
        
    def exportFile(self):
        if os.path.isfile (self.pp.text()):
            filename = QtGui.QFileDialog.getSaveFileName(self, "Save file", "", ".P00")
            self.Data.saveP00(filename)
        if os.path.isdir(self.pp.text()):
            self.Data.makeP00s()
            
        
    def openDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', os.getenv('HOME'))
        self.Data = proj.analyse()
        self.Data.setFilelist(dirname)
        self.pp.setText(dirname)
        self.out.setText(dirname + '/P00')

        
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
