# dtd2schema.py
# $Id: dtdapi.py 1 2005-09-29 15:02:35Z mccutchen $

"""
Quick-and-dirty conversion from a DTD to a very
particular schema format
"""

from xml.parsers.xmlproc import dtdparser
import cElementTree as ElementTree

from wrm.decorators import cached

class ScheduleXMLDocument:
    
    #dtdpath = 'http://www.brookhavencollege.edu/xml/schedule.dtd'
    dtdpath = 'schedule.dtd'
    xmlns = 'http://www.brookhavencollege.edu/xml/'
    
    def __init__(self):
        self.dtd = dtdparser.load_dtd(self.dtdpath)
        self.root = ElementTree.Element('schedule',xmlns=self.xmlns)
        self.tree = ElementTree.ElementTree(root)
    
    def add_element(self, parent, name, attrs={}, children=[]):
        assert isinstance(attrs, dict) or attrs is None
        assert isinstance(children, list) or children is None
        
        if parent is None:
            parent = self.root
        
        # is this a valid child element?
        dtdparent = self.dtd.elems[parent.tag]
        assert name in dtdparent.get_valid_elements(dtdparent.get_start_state())
        
        # get the valid attributes and children
        # (inserting default values where applicable)
        attrs = self.valid_attrs(name, attrs)
        children = self.valid_children(name, children)
        
        # create and return the new element
        return self.create_element(parent, name, attrs)

    @cached
    def create_element(self, parent, name, attrs=None, children=None):
        name = unicodeize(name)
        attrs = unicodeize(attrs)
        
        # create the element and its attributes
        element = SubElement(parent, name, **attrs)
        
        # add any children as simple text-only children
        for childname, childvalue in children:
            SubElement(element, childname).text = childvalue
        
        return element
    
    def valid_attrs(self, elementname, attrs):
        """
        gets all of the valid attributes out of the
        given attrs, adding default attributes where
        applicable
        """        
        dtdelement = self.dtd.elems[elementname]
        validattrs = dtdelement.attrlist
        requiredattrs = self.get_required_attrs(elementname)
        defaultattrs = dtdelement.get_default_attributes()

        validated = []

        # are all the required attributes given?
        for required in requiredattrs:
            if required not in attrs:
                raise AssertionError, "Missing required attribute '%s'" % required

        # add the valid attributes to goodattrs
        for name, value in attrs.keys():
            if name in validattrs:
                validated[name] = value

        # check to see if we're missing any defaults
        for name, value in defaultattrs:
            if name not in validated:
                validated[name] = value
        
        # return a dict of validated attributes
        return validated
    
    def valid_children(self, elementname, children):
        """
        TODO: This should check to see if all of the required
        children are present, or if there are too many children,
        etc.
        """
        return children
    
    @cached
    def get_required_attrs(self, elementname):
        required = list()
        for attr in self.dtd.elems[elementname].attrhash.values():
            if attr.decl == '#REQUIRED':
                required.append(attr.name)
        return required


class DtdApi:
    
    def __init__(self, dtdpath):
        self.dtd = dtdparser.load_dtd(dtdpath)
    
    def add_element(self, parent, name, attrs=[], children=[]):
        """
        expects attrs and children to be lists of tuples, like so:
            attrs = [(attrname, attrvalue), (attrname, attrvalue)]
            children = [(childname, childvalue), (childname, childvalue)]
        """
        assert isinstance(attrs, list) and isinstance(children, list)
        
        # is this a valid child element?
        dtdparent = self.dtd.elems[parent.tag]
        assert name in dtdparent.get_valid_elements(dtdparent.get_start_state())
        
        attrs = self.filter_attributes(name, attrs)
        children = self.filter_children(name, children)
        
        return self.create_element(parent, name, attrs)

    def filter_attributes(self, elementname, attrs):
        """
        gets all of the valid attributes out of the
        given attrs
        """
        
        dtdelement = self.dtd.elems[elementname]
        validattrs = dtdelement.attrlist
        requiredattrs = self.get_required_attrs(elementname)
        defaultattrs = dtdelement.get_default_attributes()

        filteredattrs = []

        # are all the required attributes given?
        givenattrs = [name for name, value in attrs] # extract the attribute names
        for required in requiredattrs:
            if required not in givenattrs:
                raise AssertionError, "Missing required attribute '%s'" % required

        # add the valid attributes to goodattrs
        for name, value in attrs:
            if name in validattrs:
                filteredattrs.append((name, value))

        # check to see if we're missing any defaults
        for name, value in defaultattrs:
            if name not in filteredattrs:
                filteredattrs.append((name, value))

        return filteredattrs
    
    def filter_children(self, elementname, children):
        """
        TODO: This should check to see if all of the required
        children are present, or if there are too many children,
        etc.
        """
        return children

    @cached
    def get_required_attrs(self, elementname):
        required = list()
        for attr in self.dtd.elems[elementname].attrhash.values():
            if attr.decl == '#REQUIRED':
                required.append(attr.name)
        return required
    
    def create_element(self, parent, tagname, attrs):
        print 'Creating child <%s> of parent %s' % (tagname, parent)
        return ElementTree.SubElement(parent, tagname, **dict(attrs))



if __name__ == '__main__':
    dtdpath = 'http://www.brookhavencollege.edu/xml/schedule.dtd'
    api = AutoXmlApi(dtdpath)
    
    root = ElementTree.Element('schedule')
    tree = ElementTree.ElementTree(root)
    
    term = api.add_element(root, 'term', [('name','summer1')])
    
    print term