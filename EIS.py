import sys
from PyQt4 import QtGui, QtCore
import fra
import os
import proj



class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(450, 150)
        self.setWindowTitle('EIS')
        self.setWindowIcon(QtGui.QIcon('gui/img/logo.png'))
        
#
        self.label1 = QtGui.QLabel("Input Path", self)
        self.label1.move(10, 30)
        
        self.label2 = QtGui.QLabel("Export Path", self)
        self.label2.move(10, 60)
#
        #input
        self.pp = QtGui.QLineEdit(self)
        self.pp.setGeometry(100, 30, 200, 20)
        self.pp.setEnabled(False)
        
        #output
        self.out = QtGui.QLineEdit(self)
        self.out.setGeometry(100, 60, 200, 20)
        self.out.setEnabled(False)

        exit = QtGui.QAction(QtGui.QIcon(''), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        

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
        file.addAction(openDirAction)
        file.addAction(exportAction)


        
    def exportFile(self):
        if os.path.isdir(self.pp.text()):
            self.Data.makeP00s()
            
        
    def openDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', os.getenv('HOME'))
        self.Data = proj.analyse()
        self.Data.setFilelist(dirname)
        for files in os.listdir(dirname):
            if os.path.splitext(files)[1] == '.dfr':
                self.Data.setData(dirname + '\\' +files)
        self.pp.setText(dirname)
        self.out.setText(dirname + '\P00')

        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
