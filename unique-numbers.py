
infile = file('latest.txt')
numbers = []

if __name__ == '__main__':
    print 'Duplicates'
    print '=========='

    count = dupes = 0
    for line in input:
        number = '%s-%s-%s' % (line[10:17].strip(), line[17:24].strip(), line[24:29].strip())
        if number in numbers:
            print number
            dupes += 1
        numbers.append(number)
        count += 1

    if dupes is 0:
        print '(none)'
        print

    print 'Summary'
    print '======='
    print '%d class(es)' % count
    print '%d duplicate numbers.' % dupes
        
