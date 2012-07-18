import string
import re

def parse(line):
    pattern = re.compile('(.+?)(?:\s{2,}|\n+)')
    tmpfields = pattern.findall(line)
    return tmpfields

def htmlize(line):
    line = line.replace(' ', '<span>-</span>')
    line = line.replace('\t', '<span>-\\t-</span>')
    line = line.replace('&', '&amp;')
    line = line.replace('\n','<span>-\\n-</span>')
    return line

if __name__ == "__main__":
    testfile = file("C:\\Documents and Settings\\wrm2110\\My Documents\\bh2005sp.txt")
    for i in range(10):
        print htmlize(testfile.readline())
