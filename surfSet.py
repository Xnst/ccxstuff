fin = open('skarMeshX.inp', 'r')
fut = open('skarMeshXS.inp', 'w')


def saveD(line):
    eli = line[:-1].split(',')
    elnum = int(eli[0].strip())
    uteli = []
    i = 0
    for item in eli[1:]:
        i += 1
        if len(item.strip()) > 0:
            uteli.append(int(item.strip()))

    return elnum, uteli

def esetty(line):
    neli = line[:-1].split(',')
    utli = []
    for item in neli:
        if len(item.strip()) > 0:
            utli.append(int(item.strip()))

    return utli


first = True
el2Dsave = False
el3Dsave = False
essave = False
el2D = {}
el3D = {}
esdict = {}
for line in fin:
    if "*" in line:
        first = True
        el2Dsave = False
        el3Dsave = False
        essave = False
    if '*ELEMENT' in line:
        first = True
        if "CPS3" in line:
            el2Dsave = True
            el3Dsave = False
        if "C3D4" in line:
            el2Dsave = False
            el3Dsave = True
        
        elsave = True
        essave = False

    if '*ELSET' in line:
        elis = line.split('=')
        esetName = elis[-1][:-1]
        esdict[esetName] = []
        print(esetName)
        first = True
        el2Dsave = False
        el3Dsave = False
        essave = True

    if el2Dsave:
        if first:
            first = False
        else:
            qw = saveD(line)
            el2D[qw[0]] = qw[1]
    if el3Dsave:
        if first:
            first = False
        else:
            qw = saveD(line)
            el3D[qw[0]] = qw[1]
    if essave:
        if first:
            first = False
        else:
            esdict[esetName].extend(esetty(line))


surnam = {3: 'S1', 4: 'S2', 6: 'S3', 5: 'S4'}
# surnam = {7: 'S1', 11: 'S2', 14: 'S3', 13: 'S4'}
print(esdict.keys(), len(esdict['backSkar']))
# print(esdict['backSkar'])
for key in esdict.keys():
    fut.write('*SURFACE, NAME={}\n'.format(key))
    for elly in esdict[key]:
        nodes = el2D[elly]
        e3 = []
        for el in el3D.keys():
            if nodes[0] in el3D[el]:
                e3.append(el)
        e3a = []
        for ew in e3:
            if nodes[1] in el3D[ew]:
                e3a.append(ew)
        e3b = []
        for ew in e3a:
            if nodes[2] in el3D[ew]:
                e3b.append(ew)

        nlist3 = el3D[e3b[0]]

        sval = 0
        for i in nodes:
            sval += nlist3.index(i)
        
        utstr = '{}, {}\n'.format(e3b[0], surnam[sval])

fut.close()
fin.close()

