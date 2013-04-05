import re

class analyse:
    def saveP00 (self, table, filename):
        header = 'f/Hz\tZ\'/Ohm\t-Z\'\'/Ohm\tEdc/V\tIdc/A\ttime/s\n'
        fobj = open(filename, 'w')
        fobj.write (header)
        for l in table:
            fobj.write (l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + l[3] + '\t' + l[4] + '\t' + l[5] + '\n')
        fobj.close()
        
    def loadP00(self, filename):
        Inhalt = []
        fobj = open (filename, 'r')
        for line in fobj: 
            #read file and remove Whitespace
            Inhalt.append (line.split())
        fobj.close()
        Inhalt.pop(0)
        return (Inhalt)
