import fra
import os

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
        key = os.path.splitext(os.path.basename(filename))[0]
        self.Data.update ({key : ff.Table})
        
                
    def makeP00s(self, subdir='P00'):
        if not (os.path.exists(self.Path + '/P00')):
            os.mkdir(self.Path + '/P00')
            print ('/P00 created')
        else:
            print ('/P00 already exists')
            
        #for files in self.Filelist:
        #    ff = fra.Data()
        #    ff.openFile(self.Path + '/' + files)
        #    ff.saveP00(self.Path + '/'+ subdir + '/' + os.path.splitext(files)[0]+'.P00') 
        for key in self.Data:
            ff = fra.Data()
            ff.setData(self.Data[key])
            self.Data[key]
            ff.saveP00(self.Path + '/'+ subdir + '/' + key+'.P00') 

if __name__ == '__main__':
    p = analyse()
    p.setFilelist('H:/Data/EIS/test')
    p.makeP00s()
    
 
