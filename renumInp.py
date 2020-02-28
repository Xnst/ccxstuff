n0 = 20000
e0 = 150000

fin = open('skarMesh.inp', 'r')
fut = open('skarMeshX.inp', 'w')


def nodeWrite(line, n0):
    nli = line.split(',')
    nodnum = int(nli[0].strip())
    nynum = nodnum + n0
    nli[0] = str(nynum)
    return ','.join(nli)


def elementWrite(line, e0, n0):
    eli = line.split(',')
    elnum = int(eli[0].strip())
    nynum = elnum + e0
    eli[0] = str(nynum)
    i = 0
    for item in eli[1:]:
        i += 1
        if len(item.strip()) > 0:
            eli[i] = str(int(item.strip()) + n0)

    return ','.join(eli)

def nelsetWrite(line, ne0):
    neli = line.split(',')
    i = 0
    for item in neli:
        if len(item.strip()) > 0:
            neli[i] = str(int(item.strip()) + ne0)
        i += 1

    return ','.join(neli)


first = True
nwrite = False
ewrite = False
nswrite = False
eswrite = False
for line in fin:
    if '*NODE' in line:
        first = True
        nwrite = True
        ewrite = False
        nswrite = False
        eswrite = False
        fut.write(line)
    if '*ELEMENT' in line:
        first = True
        nwrite = False
        ewrite = True
        nswrite = False
        eswrite = False
        fut.write(line)
    if '*NSET' in line:
        first = True
        nwrite = False
        ewrite = False
        nswrite = True
        eswrite = False
        fut.write(line)
    if '*ELSET' in line:
        first = True
        nwrite = False
        ewrite = False
        nswrite = False
        eswrite = True
        fut.write(line)
    if nwrite:
        if first:
            first = False
        else:
            fut.write(nodeWrite(line, n0))
    if ewrite:
        if first:
            first = False
        else:
            fut.write(elementWrite(line, e0, n0))
    if nswrite:
        if first:
            first = False
        else:
            fut.write(nelsetWrite(line, n0))
    if eswrite:
        if first:
            first = False
        else:
            fut.write(nelsetWrite(line, e0))


fut.close()
fin.close()
