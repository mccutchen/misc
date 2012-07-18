import os
import re
import urllib2


current = ''
queue = []
checked = []
bad_links = dict()

parseable_extensions = ['html','htm','css','js']


def extract_links(s):
    #link_pattern = re.compile('=[\'"]?(\S*\.(?:html|htm|css|js|gif|jpeg|jpg))[\'"]')
    link_pattern = re.compile('(?:src|href)="+(\S*)"+')
    return link_pattern.findall(s)

def find_parseable_files(root):
    """ generator function """
    candidates = []
    for root, directories, files in os.walk(root, True):
        for f in files:
            if os.path.splitext(f)[1][1:] in parseable_extensions:
                yield os.path.join(root, f)

def check_links(filename):
    if filename not in checked:

        checked.append(filename)
        links = extract_links(file(filename).read())
        print "Found %d links in %s..." % (len(links), filename)
        
        for link in links:
            if link not in checked:
                checked.append(link)
                if link.find('http://') is -1:
                    check_local_link(link, filename)
                else:
                    check_remote_link(link, filename)
            else:
                pass
                #print "\tSkipping previously checked link: %s" % link


def check_remote_link(uri, filename):
    if uri.rfind('#') is not -1:
        uri = uri[:uri.rfind('#')]
    
    request = urllib2.Request(uri)
    request.add_header("User-Agent", 'Will-bot')

    print "\tChecking %s... " % uri,
    
    try:
        response = urllib2.urlopen(request)
        print "HTTP 200 OK"
        return "HTTP 200 OK"
    except urllib2.HTTPError, e:
        add_bad_link(uri, filename, e)
        print e
        return e
    except urllib2.URLError:
        add_bad_link(uri, filename, "Host not found")
        print "Host not found"
        return "Host not found"

def check_local_link(uri, filename):
    pass
    # print "\tSkipping relative link: %s" % uri

def add_bad_link(uri, source, error):
    if source not in bad_links.keys():
        bad_links[source] = []
    bad_links[source].append((uri, error))


if __name__ == "__main__":
    
    for f in find_parseable_files("C:\\Documents and Settings\wrm2110\My Documents\Scratch"):
        check_links(f)

    print "Checked: %s" % len(checked)
    print "Documents containing bad links %s" % len(bad_links)
    print
    print "Problems:"
    for doc in bad_links.keys():
        print "\t%s, 0" % doc
        for link in bad_links[doc]:
            print "\t\tLink: %s, Error: %s" % link
