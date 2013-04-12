import os
import re
import mod.pfr as pfr
import mod.dfr as dfr
import mod.p00 as p00
from pylab import *
from scipy import *
from scipy import optimize
import numpy as np
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
            self.Table = dfr.makeTable(dfrfile)
            print ('File opened:' + filepath)
        else:
            return (False)
        return (True)
    
    ##
    # Saves the Table in the P00 filestructure
    def saveP00 (self, filename):
        p00.saveP00(self.Table, filename)
        print ('File exported: ' + filename)
        
    ##
    # analyses the P00 file and sets the Table Variable
    def __makeTablefromP00 (self, filename):
        try:
            self.Table = p00.loadP00(filename)
            print ('Data Imported from: ' +filename)
        except:
            print ('Import file failed: ' + filename)
        


    def setData(self, table):
        self.Table = table

    def simpleFit(self):
       
        flist = []
        zlist = []
        
        import math
        for i in self.Table:
            flist.append((float(i[0])))
            zlist.append((math.sqrt(float(i[1])**2+float(i[2])**2)))
        f = np.array(flist)
        z = np.array(zlist)
        fitfunc   = lambda p, x  : abs(p[0] + 1/(1/p[1] - 1j*2*math.pi*p[2]*x))
        errfunc = lambda p, x, y: fitfunc(p, x) - y
        p0 = [ z[1], z[-1], 1e-7]
        p1, success = optimize.leastsq(errfunc, p0[:], args=(f, z))
        print (p1)
        
        #print (success)
        
        print (p0)
        
        
        
        
if __name__ == '__main__':
    a = Data()
    a.openFile(r'H:\Data\EIS\test\-900MV.pfr')
    #print (a.Table)
    a.simpleFit()



