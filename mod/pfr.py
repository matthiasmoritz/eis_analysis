import re
class analyse:
    mapping = None
    def setData(self, filepath):
        self.mapping = {}
        Inhalt = []
        fobj = open (filepath, "r")
        for line in fobj: 
            #read file and remove Whitespace
            Inhalt.append (re.sub(' ','',(line).strip('\n')))
        fobj.close()
        self.mapping = {}
        j=''
        for i in Inhalt:
            if "[" in i:
                j = i.strip('[').strip(']')
                self.mapping.update ({j: {}})
            if "=" in i:
                l={}
                k = i.split('=')
                l = {k[0]:k[1]}
                self.mapping[j].update(l)

         
    def potential(self):    
        """reads the offsetpotential from a dfr file"""
        return (self.mapping["PotentiostaticSingle"]["Potential"])


if __name__ =='__main__':
    pp = pfr()
    pp.setData(r'\\wsi\e25\Home\matthias.moritz\My Documents\Data\EIS\test\400MV.pfr')
    print (pp.potential())
