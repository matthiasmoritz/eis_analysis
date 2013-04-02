class analyse:
    def saveP00 (self, table, filename):
        header = 'f/Hz\tZ\'/Ohm\t-Z\'\'/Ohm\tEdc/V\tIdc/A\ttime/s\n'
        print (header)
        fobj = open(filename, 'w')
        fobj.write (header)
        
        for l in table:
            fobj.write (l[0] + '\t' + l[1] + '\t' + l[2] + '\t' + l[3] + '\t' + l[4] + '\t' + l[5] + '\n')
        fobj.close()
