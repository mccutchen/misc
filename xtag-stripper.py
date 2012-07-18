import re

inpath = 'NUTR.xtg'
outpath = 'NUTR.txt'

tagpattern = r'@[A-Za-z ]+:'
replacepattern = ''

data = file(inpath).read()
data = re.sub(tagpattern, replacepattern, data)

file(outpath, 'w').write(data)
    