# dtd2schema.py
# $Id: dtd2schema.py 1 2005-09-29 15:02:35Z mccutchen $

"""
Quick-and-dirty conversion from a DTD to a very
particular schema format
"""

attr_separator = '_'
child_separator = '_'

from xml.parsers.xmlproc import dtdparser

dtd = dtdparser.load_dtd('schedule.dtd')

for name, element in dtd.elems.items():
    for attr in element.attrlist:
        output = '%s%s%s = ' % (name, attr_separator, attr)
        print output
    for child in element.get_valid_elements(element.get_start_state()):
        output = '%s%s%s = ' % (name, child_separator, child)
        print output
