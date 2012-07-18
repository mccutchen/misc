import os
import shutil
import glob

def copyfiles(sourcedir, destdir, patterns = '*'):
    """
    Copies files and directories which match pattern
    from sourcedir into destdir, recreating directory
    structure as necessary.

    patterns should be a space-separated list of patterns
    to feed to glob.glob()
    """
    if not os.path.isdir(sourcedir):
        raise IOError, 'sourcedir must exist and must be a directory.'

    if not os.path.exists(destdir):
        os.mkdir(destdir)
    else:
        if not os.path.isdir(destdir):
            raise IOError, 'If destdir exists, it must be a directory'

    # remember where we started
    cwd = os.getcwd()

    # get the paths to the files we want to copy
    os.chdir(sourcedir)
    files = []
    for pattern in patterns.split():
        files.extend(glob.glob(pattern))
    os.chdir(cwd)

    # copy the files
    for f in files:
        dest = destdir
        path, name = os.path.split(f)

        # do we need to copy this file to a subdirectory?
        if path:
            # create the subdirectory under destdir to hold the
            # file, if it doesn't exist
            if not os.path.exists(os.path.join(destdir, path)):
                os.chdir(destdir)
                os.makedirs(path)
                os.chdir(cwd)
                
            # add the subdirectory to the destination path
            dest = os.path.join(destdir, path)

        # add the source directory to the file path
        f = os.path.join(sourcedir, f)

        # copy the file
        shutil.copy2(f, dest)


if __name__ == '__main__':
    src = 'copytest'
    dest = 'xdest'

    copyfiles(src, dest, '*.txt css/*.css')
