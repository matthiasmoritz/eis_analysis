import sys
from PyQt4 import QtGui, QtCore
import fra
import os
import proj




class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self)

        self.resize(450, 200)
        self.setWindowTitle('EIS')
        self.setWindowIcon(QtGui.QIcon('gui/img/logo.png'))
        
        #Path to the Imported Files
        self.label1 = QtGui.QLabel("Input Path", self)
        self.label1.move(10, 30)

        self.pp = QtGui.QLineEdit(self)
        self.pp.setGeometry(100, 30, 200, 20)
        self.pp.setEnabled(False)
        
        #Target Path for the  Export
        self.label2 = QtGui.QLabel("P00 Path", self)
        self.label2.move(10, 60)

        self.p00 = QtGui.QLineEdit(self)
        self.p00.setGeometry(100, 60, 200, 20)
        self.p00.setEnabled(False)
        
        self.label3 = QtGui.QLabel("Analyse Path", self)
        self.label3.move(10, 90)
        self.anal = QtGui.QLineEdit(self)
        self.anal.setGeometry(100, 90, 200, 20)
        self.anal.setEnabled(False)
        
        self.label4 = QtGui.QLabel("Area", self)
        self.label4.move(10, 120)
        self.area = QtGui.QLineEdit(self)
        self.area.setGeometry(100, 120, 200, 20)
        self.area.setEnabled(True)
        self.area.setText('0.196')        

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
        self.Data.makeImpTable(float(self.area.text()))
        self.Data.makePhaseTable()
        self.Data.makeMottSchottky(float(self.area.text()))
        
            
        
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
            self.p00.setText(dirname + '\P00')
            self.anal.setText(dirname + '\analyse')
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
    
