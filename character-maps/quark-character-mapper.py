# $id$

"""
Creates a list of <xsl:output-character /> elements
to be used inside an <xsl:character-map /> to provide
a mapping from the Latin-1 Unicode characters to their
ISO-8859-1 counterparts, in Quark Xpress Xtag format,
which looks like this: <\#227>.

Did that make sense?
"""

inpath = '8859-1.txt'
outpath = 'xml-character-mapping.txt'

template = '<xsl:output-character character="%s" string="%s" /> <!-- %s -->'


def entitize(n):
    return '&#%s;' % n.strip().lstrip('0')

def xtagize(n):
    return '&lt;\#%d&gt;' % int(n.strip(), 16)

mappings = list()
for line in (line.strip() for line in file(inpath) if not line.startswith('#')):
    fields = line.split('\t')
    iso = xtagize(fields[0])
    utf = entitize(fields[1])
    comment = fields[3].strip()
    mappings.append((utf, iso, comment))

outfile = file(outpath, 'w')
for mapping in mappings:
    print >> outfile, template % mapping