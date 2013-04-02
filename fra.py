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
    def setData (self, filepath):
        extension = os.path.splitext(filepath)[1]
        if extension == '.P00':
            self.__makeTablefromP00(filepath)
        if extension == '.dfr' or extension == '.pfr':
            dfrfile = os.path.splitext(filepath)[0] + '.dfr'
            dd = mod.dfr.analyse()
            self.Table = dd.table(dfrfile)
        else:
            return (False)
        return (True)
    
    ##
    # Saves the Table in the P00 filestructure
    def saveP00 (self, filename):
        dat = mod.p00.analyse()
        dat.saveP00(self.Table, filename)
        
    ##
    # analyses the P00 file and sets the Table Variable
    def __makeTablefromP00 (self, filepath):

        print ('P00')


    def getPotential(self, filepath):
        (path, filename) = os.path.split(filepath)
        pfrfile = os.path.splitext(filepath)[0] + '.pfr'
        pp = mod.pfr.analyse()
        pp.setData(pfrfile)
        potential = pp.potential()

b = Data()
b.setData(r'\\wsi\e25\Home\matthias.moritz\My Documents\Data\EIS\test\400MV.pfr')
b.saveP00(r'\\wsi\e25\Home\matthias.moritz\My Documents\Data\EIS\test\P00\400mV.P00_1')

