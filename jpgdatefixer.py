import datetime, glob, os, re, sys
import EXIF

DIR_DATE_PATTERN = r'.*(\d{4})-(\d{2})-(\d{2}).*'
EXIF_DATE_PATTERN = r'(\d{4}):(\d{2}):(\d{2}).*'
EXIF_BAD_DATE_PATTERN = r'0000:00:00 00:00:00'
IMAGE_FILE_PATTERN = r'dscn*.jpg'

JHEAD_DATE_FORMAT = '%Y:%m:%d-12:00:00'
JHEAD_CMD = 'jhead -ts%(date)s %(files)s'

root = os.path.expanduser('~/Desktop/Old Photos/')
assert os.path.exists(root) and os.path.isdir(root)

def main():
    for dirname, subdirs, filenames in os.walk(root):
        
        print 'Inspecting %s...' % dirname,
        if not is_valid_image_directory(dirname):
            print 'Not a valid directory.'
            continue

        images_to_fix, nonfixers = should_fix_dates(dirname)
        print '%d images to fix (%d to skip).' % (len(images_to_fix), len(nonfixers))
        
        correct_date = parse_directory_date(dirname).strftime(JHEAD_DATE_FORMAT)
        print ' - Using jhead to fix images...',
        
        args = {
            'date': correct_date,
            'files': ' '.join(images_to_fix)
        }
        result = os.system(JHEAD_CMD % args)
        print 'Finished (%s)' % result
            

def should_fix_dates(directory):
    """Extracts the expected date from the directory name and sets
    that as the EXIF date on the contained image files if they don't
    already have an EXIF date set."""
    if not is_valid_image_directory(directory):
        return []
    
    os.chdir(directory)
    images = glob.glob(IMAGE_FILE_PATTERN)
    
    # only return images that don't have their EXIF date set
    fixers = filter(lambda img: get_exif_date(img) is None, images)
    nonfixers = filter(lambda img: get_exif_date(img) is not None, images)
    
    return fixers, nonfixers

def get_exif_date(filename):
    """Gets a datetime.date object from the given EXIF data."""
    exifdata = get_exif_data(filename)
    datekeys = [
        'Image DateTime',
        'EXIF DateTimeOriginal',
        'EXIF DateTimeDigitized'
    ]
    dates = []
    for key in datekeys:
        dates.append(exifdata[key].printable)
    if validate_exif_dates(dates):
        return make_date(re.match(EXIF_DATE_PATTERN, dates[0]))
    else:
        return None

def get_exif_data(filename):
    """Returns a dict of EXIF data for the given image file."""
    assert os.path.exists(filename), 'File not found: %s' % filename
    infile = open(filename, 'rb')
    exifdata = EXIF.process_file(infile)
    infile.close()
    return exifdata

def validate_exif_dates(dates):
    """Ensures that all of the dates in the given EXIF data are the same, and that each one matches EXIF_DATE_PATTERN."""
    for date in dates:
        assert date is not None, 'Invalid (null) date given.'
        assert date == dates[0], 'Date %s does not match the first date, %s' % (date, dates[0])
        #print date, type(EXIF_DATE_PATTERN)
        assert re.match(EXIF_DATE_PATTERN, date), 'Date %s does not match the EXIF date pattern /%s/' % (date, EXIF_DATE_PATTERN)
    
    if re.match(EXIF_BAD_DATE_PATTERN, date):
        return False
    else:
        return True

def is_valid_image_directory(dirname):
    """Returns true if the given directory name matches DIR_DATE_PATTERN."""
    return re.match(DIR_DATE_PATTERN, dirname) is not None
    
def parse_directory_date(dirname):
    """Parses a datetime.date object out of the given file name, which
    is expected to be in "YYYY-MM-DD (Description)" format."""
    match = re.match(DIR_DATE_PATTERN, dirname)
    assert match, 'The given directory name (%s) did not match the regular expression /%s/' % (dirname, DIR_DATE_PATTERN)
    return datetime.date(*map(int, match.groups()))

def make_date(match):
    """Creates a datetime.date object from the given regex match object, which should have exactly three groups: year, month, day."""
    groups = match.groups()
    assert len(groups) is 3, 'The given match object must have exactly three groups: year, month, day.  Given groups: %s' % ','.join(groups)
    return datetime.date(*map(int, groups))
    

if __name__ == '__main__':
    main()