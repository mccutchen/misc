import os, sys

SVNDIR = '.svn'
DELCMD = 'rd /S /Q %s'

def unsvn(arg, dirname, filenames):
    if SVNDIR in filenames:
        svnpath = os.path.join(dirname, SVNDIR)
        cmd = DELCMD % svnpath
        
        # open the command as a subprocess
        stdin, stdout, stderr = os.popen3(cmd)
        
        # collect the actual messages
        stdout, stderr = [stream.read() for stream in (stdout, stderr)]
        
        if stderr.strip():
            print ' ! Error: %s (command: %s)' % (stderr, cmd)
        else:
            print 'Cleaned %s ...' % dirname
        
        # remove the svn directory from the filenames list
        filenames.remove(SVNDIR)

def main():
    os.path.walk(r'.',unsvn, None)

if __name__ == '__main__':
    main()