import os, string

def parsenum(path):
    name, ext = os.path.splitext(path)
    digits = filter(numberfilter, iter(path))
    return int(''.join(digits))

def numberfilter(s):
    return s in string.digits

def jpgfilter(name):
    return name.endswith('.jpg')

def pad(s, padder='0', targetlength=3):
    length = len(str(s))
    if length < targetlength:
        diff = targetlength - length
        s = '%s%s' % (padder * diff, s)
    return s

def slidesort(s1, s2):
    return cmp(parsenum(s1), parsenum(s2))

def newname(oldname, prefix='img', padder='0', padlength=3):
    prefix = 'img'
    suffix = '.jpg'
    name = prefix + pad(parsenum(oldname), padder, padlength) + suffix
    return name


slides = filter(jpgfilter, os.listdir('.'))
print 'Unsorted slides:'
print slides

slides.sort(slidesort)

print 'Sorted slides:'
print slides

print 'Renaming slides...'
for slide in slides:
    newslide = newname(slide)
    print '\t%s -> %s' % (slide, newslide)
    os.rename(slide, newslide)
