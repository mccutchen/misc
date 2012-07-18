import os

extensions = '.htm .html .aspx .pdf'.split()
skipdirs = '.svn'.split()

filecount = 0
typecount = dict()
for ext in extensions:
    typecount[ext] = 0

def countfiles(arg, dirname, filenames):
    global filecount, typecount, skipdirs
    if dirname not in skipdirs:
        print ' - %s' % dirname
        for name, ext in map(os.path.splitext, filenames):
            if ext in extensions:
                filecount += 1
                typecount[ext] += 1

def main():
    print 'Counting files ...'
    os.path.walk(r'.',countfiles, None)
    print 'Finished.'
    print
    
    print 'Total file count: %d' % filecount
    print '---'
    print 'Extension counts:'
    for ext, count in typecount.items():
        print ' - %s: %d' % (ext, count)

if __name__ == '__main__':
    main()
