
outfile = file('out.xml','w')
for line in file('regroupings.xml'):
    if line.strip():
        print >> outfile, line.rstrip()