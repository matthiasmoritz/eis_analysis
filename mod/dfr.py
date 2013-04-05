import re

def makeTable(filepath):
    Inhalt = []
    fobj = open(filepath, 'r')
    for line in fobj: 
        #read file and remove Whitespace
        Inhalt.append (re.sub(' ','',(line).strip('\n')))
    fobj.close()

    #remove bullshitdata from the drf file
    #some of the enterys are just no measurement data
    i = 0
    while i*6 < len(Inhalt):
        for x in range (3):
            Inhalt.pop(i*6)
        i +=1
    for i in range (6):
        Inhalt.pop(len(Inhalt)-1)

    Table = []
    for x in range (int(len(Inhalt)/6)):
        Table.append([Inhalt[x*6],  Inhalt[x*6+1], Inhalt[x*6+2], Inhalt[x*6+3], Inhalt[x*6+4], Inhalt[x*6+5]])

    return (Table)
