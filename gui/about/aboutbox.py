import sys
from PyQt4 import QtGui, QtCore

class about(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        
        self.getInfo()
        self.initUI()

        
    def initUI(self):      
        self.setWindowTitle('About EIS')
        self.setGeometry(300, 300, 250, 150)
        
        
        ok = QtGui.QPushButton('Ok', self)
        ok.setCheckable(True)
        ok.move(10, 120)
        ok.show()
        ok.clicked.connect(self.buttonClicked)
        self.show()
        
    def getInfo(self):
        self.label1 = QtGui.QLabel("EIS-analyser", self)
        self.label1.move(10, 15)        
                
        self.label2 = QtGui.QLabel("Version 0.2", self)
        self.label2.move(10, 30) 
        
        self.label3 = QtGui.QLabel("Matthias Moritz <moritz370@googlemail.com>", self)
        self.label3.move(10, 45) 
        
        self.label4 = QtGui.QLabel("https://github.com/matthiasmoritz/eis_analysis", self)
        self.label4.move(10, 60) 
        
    def buttonClicked(self):
        self.close()



def main():

    ab = about()
    ab.show()
    ab.exec_()
    

if __name__ == '__main__':
    
    app = QtGui.QApplication(sys.argv)
    ab = about()
    ab.show()
    (app.exec_())

    
