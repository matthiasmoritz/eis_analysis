import fra
import os
import mod.pfr

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

if __name__ == '__main__':
    p = analyse()
    #p.setFilelist('H:/Data/EIS/test')
    p.openFile(r'H:/Data/EIS/test/100MV.dfr')
    #p.makeP00s()
    
 
