import math
def getFrequencyList(Data):
    flist = []
    for key in Data:
        s = Data[key]["data"]
        for f in s:
            if float(f[0]) not in flist:
                flist.append(float(f[0]))
    return (sorted(flist))
    

def getPotentialList(Data):
    plist = []
    for key in Data:
        p = Data[key]["potential"]
        if p not in plist:
            plist.append(p)
    return (sorted(plist))


def getImpedanceTable(Data):
    flist = getFrequencyList(Data)
    plist = getPotentialList(Data)
    i = 0
    pdic = {}
    for p in plist:
        pdic.update({p:i})
        i = i+1
    i = 0
    fdic = {}
    for f in flist:
        fdic.update({str(f):i})
        i = i+1   
        
    tab = []
    for f in range(len(flist)):
        row = []
        
        for p in range (len(plist)):
            row.append('-')
        tab.append(row)
        
    for key in Data:
        for i in Data[key]["data"]:
            #print (i)
            #print (fdic[str(float(i[0]))])
            fv=(fdic[str(float(i[0]))])
            pv=(pdic[Data[key]["potential"]])
            zv=round(math.sqrt(float(i[1])**2+float(i[2])**2), 4)
            tab[fv][pv] = zv
    return (tab)
  
    
if __name__ == '__main__':
    d = {}
    d.update ({'k1':{"data" : [[1.12,0,0],[2,0,0],[3,0,0]]}})
    d['k1'].update({"potential": 0.2})
    d.update ({'k2':{"data" : [[4,0,0],[5,0,0],[3,0,0]]}})
    d['k2'].update({"potential": -0.4})
    print(getImpedanceTable(d))
