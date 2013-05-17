import fra
import os
import mod.pfr
import mod.analyse

class analyse:
    def __init__(self):
        self.Filelist = []
        self.Path = ''
        self.Data = {}
        
    def setFilelist(self, path):
        
        self.Data = {}
        self.Path = path
        for files in os.listdir(path):
            if os.path.splitext(files)[1] == '.dfr':
                self.Filelist.append(files)
                
                
    def openFile(self, filename):
        ff = fra.Data()
        ff.openFile(filename)
        basename = os.path.splitext(os.path.basename(filename))[0]
        key = filename
        #Add Data
        self.Data.update ({key :{"data": ff.Table}})
        #Add Basename
        self.Data[key].update({"basename" : basename})
        #Add Potential
        try:
            #by reading the .pfr file 
            potential = mod.pfr.potential(os.path.splitext(filename)[0]+'.pfr')
            self.Data[key].update({"potential" : float(potential)})
        except:
            #by calculating from the raw data
            av = 0
            for E in self.Data[key]["data"]:
                av = av + float(E[3])
            potential = av/len(self.Data[key]["data"])
            potential = round(potential,3)
            self.Data[key].update({"potential" : potential})
            
        #Add fitting Data
        self.Data[key].update({"fit" : ff.simpleFit()})

            
        
                
    def makeP00s(self, subdir='P00'):
        
        if not (os.path.exists(self.Path + '/P00')):
            os.mkdir(self.Path + '/P00')
            print ('/P00 created')
        else:
            print ('/P00 already exists')
        counter = 0
        try:
            for key in self.Data:
                ff = fra.Data()
                ff.setData(self.Data[key]["data"])
                ff.saveP00(self.Path + '/'+ subdir + '/' + self.Data[key]["basename"]+'.P00') 
                counter = counter+1
            print (str(counter) + ' P00 files exported to ' + self.Path + '/'+ subdir + '/')
        except (Exception, e):
            print ('P00-Error:')
            print (e)



    def makeImpTable(self, area, subdir='analyse'):
        if not (os.path.exists(self.Path + '/' + subdir)):
            os.mkdir(self.Path + '/' + subdir)
            print ('/' + subdir+ ' created')
        flist = mod.analyse.getFrequencyList(self.Data)
        plist = mod.analyse.getPotentialList(self.Data)
        tab = mod.analyse.getTable(self.Data, "impedance", area)
        header = 'f/Hz,'
        for p in plist:
            header = header + str(p) + ','
        header = header[:-1]+'\n'
        fobj = open(self.Path + '/' + subdir + '/impedancetable.imp', 'w')
        fobj.write(header)
        counter = 0
        for l in tab:
            row = str(flist[counter])+','
            for i in l:
                row = row+str(i)+','
            row = row[:-1]+'\n'
            fobj.write(row)
            counter = counter +1
        fobj.close()       
        
    def makePhaseTable(self, subdir='analyse'):
        if not (os.path.exists(self.Path + '/' + subdir)):
            os.mkdir(self.Path + '/' + subdir)
            print ('/' + subdir+ ' created')
        flist = mod.analyse.getFrequencyList(self.Data)
        plist = mod.analyse.getPotentialList(self.Data)
        tab = mod.analyse.getTable(self.Data, "phase")
        header = 'f/Hz,'
        for p in plist:
            header = header + str(p) + ','
        header = header[:-1]+'\n'
        fobj = open(self.Path + '/' + subdir + '/phasetable.phi', 'w')
        fobj.write(header)
        counter = 0
        for l in tab:
            row = str(flist[counter])+','
            for i in l:
                row = row+str(i)+','
            row = row[:-1]+'\n'
            fobj.write(row)
            counter = counter +1
        fobj.close()


    def makeMottSchottky(self, areaFactor=1, subdir='analyse'):
        msData = {}
        for key in self.Data:
            msData.update ({self.Data[key]["potential"] : self.Data[key]["fit"][0][2]})
        header = 'Potential,1/C²\nV,µF^-2*cm^4\n'
        fobj = open(self.Path + '/' + subdir + '/mottSchottky.msy', 'w')
        fobj.write(header)
        for key in sorted(msData):
            fobj.write (str(key) + ',' + str(1/(msData[key]/areaFactor)**2)+ '\n')
        fobj.close()
        

    def makeFittingTable(self, areaFactor=1, subdir ='analyse'):
        fitData = {}
        for key in self.Data:
            fitData.update({self.Data[key]["potential"] : self.Data[key]["fit"][0]})
        header = 'Potential,R_S,R_P,C\n'
        fobj = open(self.Path + '/' + subdir + '/fitting.fit', 'w')
        fobj.write (header)
        for key in sorted(fitData):
            fobj.write (str(key) + ',' + str(abs(fitData[key][0]*areaFactor)) + ','+ str(abs(fitData[key][1]*areaFactor)) + ',' + str(abs(fitData[key][2]/areaFactor)) + '\n')
        fobj.close()
            
        
if __name__ == '__main__':
    p = analyse()
    #p.setFilelist('H:/Data/EIS/test')
    p.openFile(r'H:/Data/EIS/test/-200MV.dfr')
    p.openFile(r'H:/Data/EIS/test/100MV.dfr')
    p.openFile(r'H:/Data/EIS/test/300MV.dfr')
    p.makeP00s('Data/EIS/test/P00')
    #p.makeImpTable(0.196)
    #p.makeMottSchottky(1)

    #tab =(mod.analyse.getImpedanceTable(p.Data))
    #fobj = open(r'H:/Data/EIS/test/impedtest.asdf', 'w')
    #for l in tab:
    #    fobj.write (str(l[0]) + ' ' + str(l[1]) + ' ' + str(l[2]) + '\n')
    #fobj.close()
    #p.makeP00s()
    
 
