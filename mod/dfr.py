import re

def makeTable(filepath):
    Inhalt = []
    fobj = open(filepath, 'r')
    for line in fobj: 
        #read file and remove Whitespace
        Inhalt.append (re.sub(' ','',(line).strip('\n')))
    fobj.close()
    
    frequencys = int(Inhalt[1])
    potentials = int(Inhalt[2])
    datasets = frequencys*potentials
    #remove bullshitdata from the drf file
    #some of the enterys are just no measurement data
    i = 0
    while i < datasets-1:
        for x in range (3):
            Inhalt.pop(i*6)
        i +=1
    dropitems = len(Inhalt) - datasets*6
    for i in range(dropitems):
        Inhalt.pop()

    print (len(Inhalt))
    #for i in dropitems:
    #Inhalt.pop(len(Inhalt)-1)
   
    Table = []
    Temptable = []
    counter = 0
    for k in range (int(potentials)):
        for y in range (int(frequencys)):
            Temptable.append([Inhalt[counter*6],  Inhalt[counter*6+1], Inhalt[counter*6+2], Inhalt[counter*6+3], Inhalt[counter*6+4], Inhalt[counter*6+5]])
            counter = counter +1
        Temptable.pop(len(Temptable)-1)
        Table.append(Temptable)
        Temptable = []
    return (Table)
