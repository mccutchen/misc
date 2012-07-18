"""
Used to generate appropriate htdigest thingies
for tracd.  Cribbed from:

http://projects.edgewall.com/trac/wiki/TracStandalone
"""

from optparse import OptionParser
import md5

# build the options
usage = "usage: %prog [options]"
parser = OptionParser(usage=usage)
parser.add_option("-u", "--username",action="store", dest="username", type = "string",
                  help="the username for whom to generate a password")
parser.add_option("-p", "--password",action="store", dest="password", type = "string",
                  help="the password to use")
(options, args) = parser.parse_args()

# check options
if (options.username is None) or (options.password is None):
   parser.error("You must supply both the username and password")
   
# Generate the string to enter into the htdigest file
realm = 'trac'
kd = lambda x: md5.md5(':'.join(x)).hexdigest()
print ':'.join((options.username, realm, kd([options.username, realm, options.password])))

wrm2110:trac:3f633f2e5805840f5ca3ec0c546aa9cd