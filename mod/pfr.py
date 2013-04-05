import re


def parsePfr(filepath):
    mapping = {}
    Inhalt = []
    fobj = open (filepath, "r")
    for line in fobj: 
        #read file and remove Whitespace
        Inhalt.append (re.sub(' ','',(line).strip('\n')))
    fobj.close()
    mapping = {}
    j=''
    for i in Inhalt:
        if "[" in i:
            j = i.strip('[').strip(']')
            mapping.update ({j: {}})
        if "=" in i:
            l={}
            k = i.split('=')
            l = {k[0]:k[1]}
            mapping[j].update(l)

    return (mapping)
     
def potential(filepath):    
    """reads the offsetpotential from a dfr file"""
    return (parsePfr(filepath)["PotentiostaticSingle"]["Potential"])


if __name__ =='__main__':
    print (potential(r'H:\Data\EIS\test\400MV.pfr'))
    
