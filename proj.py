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
            potential = mod.pfr.potential(os.path.splitext(filename)[0]+'.pfr')
            self.Data[key].update({"potential" : float(potential)})
        except:
            av = 0
            for E in self.Data[key]["data"]:
                av = av + float(E[3])
            potential = av/len(self.Data[key]["data"])
            potential = round(potential,3)
            self.Data[key].update({"potential" : potential})

            
        
                
    def makeP00s(self, subdir='P00'):
        if not (os.path.exists(self.Path + '/P00')):
            os.mkdir(self.Path + '/P00')
            print ('/P00 created')
        else:
            print ('/P00 already exists')

        for key in self.Data:
            ff = fra.Data()
            ff.setData(self.Data[key]["data"])
            ff.saveP00(self.Path + '/'+ subdir + '/' + self.Data[key]["basename"]+'.P00') 



    def makeImpTable(self, area, subdir='analyse'):
        if not (os.path.exists(self.Path + '/' + subdir)):
            os.mkdir(self.Path + '/' + subdir)
            print ('/' + subdir+ ' created')
        else:
            print ('/' +subdir+' already exists')
        flist = mod.analyse.getFrequencyList(self.Data)
        plist = mod.analyse.getPotentialList(self.Data)
        tab = mod.analyse.getTable(self.Data, "potential", area)
        header = 'f/Hz,'
        for p in plist:
            header = header + str(p) + ','
        header = header[:-1]+'\n'
        print (header)
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
        else:
            print ('/' +subdir+' already exists')
        flist = mod.analyse.getFrequencyList(self.Data)
        plist = mod.analyse.getPotentialList(self.Data)
        tab = mod.analyse.getTable(self.Data, "phase")
        header = 'f/Hz,'
        for p in plist:
            header = header + str(p) + ','
        header = header[:-1]+'\n'
        print (header)
        fobj = open(self.Path + '/' + subdir + '/phasetable.imp', 'w')
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


if __name__ == '__main__':
    p = analyse()
    #p.setFilelist('H:/Data/EIS/test')
    p.openFile(r'H:/Data/EIS/test/100MV.dfr')
    p.openFile(r'H:/Data/EIS/test/-200MV.dfr')
    p.openFile(r'H:/Data/EIS/test/300MV.dfr')
    p.makeImpTable()
    #tab =(mod.analyse.getImpedanceTable(p.Data))
    #fobj = open(r'H:/Data/EIS/test/impedtest.asdf', 'w')
    #for l in tab:
    #    fobj.write (str(l[0]) + ' ' + str(l[1]) + ' ' + str(l[2]) + '\n')
    #fobj.close()
    #p.makeP00s()
    
 
