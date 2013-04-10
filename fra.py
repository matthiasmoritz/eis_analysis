import os
import re
import mod.pfr
import mod.dfr
import mod.p00
##
# @brief This class gets the content of the *.dfr and *.pfr files and makes a P00 file
#
class Data:
    
    def __init__(self):
        self.Table = None 
    
    ##
    # @brief Sets The Table Variable of the object
    # Call with one of the following Filetypes
    # @li *.P00
    # @li *.dfr
    # @li *.pfr
    # 
    def openFile (self, filepath):
        extension = os.path.splitext(filepath)[1]
        if extension == '.P00':
            self.__makeTablefromP00(filepath)
        if extension == '.dfr' or extension == '.pfr':
            dfrfile = os.path.splitext(filepath)[0] + '.dfr'
            self.Table = mod.dfr.makeTable(dfrfile)
            print ('File opened:' + filepath)
        else:
            return (False)
        return (True)
    
    ##
    # Saves the Table in the P00 filestructure
    def saveP00 (self, filename):
        mod.p00.saveP00(self.Table, filename)
        print ('File exported: ' + filename)
        
    ##
    # analyses the P00 file and sets the Table Variable
    def __makeTablefromP00 (self, filename):
        try:
            self.Table = mod.p00.loadP00(filename)
            print ('Data Imported from: ' +filename)
        except:
            print ('Import file failed: ' + filename)
        


    def setData(self, table):
        self.Table = table


if __name__ == '__main__':
    a = Data()
    print (float(a.getPotential(r'H:\Data\EIS\test\400MV.pfr')))



