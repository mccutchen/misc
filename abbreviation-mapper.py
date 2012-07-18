import csv


mappings = dict()

reader = csv.reader(file('District Abbreviations.csv'))
for rubrik, name in reader:
    mappings.setdefault(name, list())
    mappings[name].append(rubrik)

outfile = file('mappings.txt','w')
for name, rubriks in mappings.items():
    line = '%s = ' % name
    for rubrik in rubriks:
        line = line + '%s ' % rubrik
    line = line.strip()
    outfile.write(line + '\n')