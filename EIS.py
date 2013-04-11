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
        
        #Path to the Imported Files
        self.label1 = QtGui.QLabel("Input Path", self)
        self.label1.move(10, 30)

        self.pp = QtGui.QLineEdit(self)
        self.pp.setGeometry(100, 30, 200, 20)
        self.pp.setEnabled(False)
        
        #Target Path for the P00 Export
        self.label2 = QtGui.QLabel("Export Path", self)
        self.label2.move(10, 60)

        self.out = QtGui.QLineEdit(self)
        self.out.setGeometry(100, 60, 200, 20)
        self.out.setEnabled(True)

        #FileMenu
        #   Exit
        exit = QtGui.QAction(QtGui.QIcon(''), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        #   Open Directory
        openDirAction = QtGui.QAction('Open Directory', self) 
        openDirAction.setStatusTip('Open a directory') 
        openDirAction.triggered.connect(self.openDir)
        #   Export (as P00)
        exportAction = QtGui.QAction('Export', self) 
        exportAction.setShortcut('Ctrl+E') 
        exportAction.setStatusTip('Export as P00 file') 
        exportAction.triggered.connect(self.exportFile)
        
        #AboutMenu
        #   About
        openAboutWidget = QtGui.QAction ('About', self)
        openAboutWidget.triggered.connect(self.aboutWidget)
        
        #Create Menu Bar
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        file.addAction(openDirAction)
        file.addAction(exportAction)
        
        about = menubar.addMenu('&About')
        about.addAction(openAboutWidget)

        self.statusBar()
        
    def exportFile(self):
        if os.path.isdir(self.pp.text()):
            self.Data.makeP00s()
        self.Data.makeImpTable()
            
        
    def openDir(self):
        dirname = QtGui.QFileDialog.getExistingDirectory(self, 'Open Directory', os.getenv(''))
        try:
            self.Data = proj.analyse()
            self.Data.setFilelist(dirname)
            for files in os.listdir(dirname):
                if os.path.splitext(files)[1] == '.dfr':
                    self.Data.openFile(dirname + '\\' +files)
                if os.path.splitext(files)[1] == '.P00':
                    self.Data.openFile(dirname + '\\' +files)
            self.pp.setText(dirname)
            self.out.setText(dirname + '\P00')
        except:
            print ('no files imported')

        
    def aboutWidget(self):
        import gui.about.aboutbox
        gui.about.aboutbox.main()

        
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    
